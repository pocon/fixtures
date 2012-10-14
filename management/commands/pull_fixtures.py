"""
A management command which Grabs MPs Twitter handles from OA

"""

from django.core.management.base import NoArgsCommand
from fixtures.models import *
from BeautifulSoup import BeautifulStoneSoup as BS
import urllib2

def grabFixtures(page):
    page = BS(urllib2.urlopen("http://www.sydgram.nsw.edu.au/co-curricular/sport/fixtures/" + page))

    table = page.find('table', {"class": "excel144"})

    sport_classes = ['excel161', 'excel148', 'excel153']

    sportmapper = {
        'excel161': {'name': "Tennis", 'school': 'excel163', 'info': 'excel164', 'index': 0},
        'excel148': {'name': "Cricket", 'school': 'excel149', 'info': 'excel157', 'index': 0},
        'excel153': {'name': "Basketball", 'school': 'excel149', 'info': 'excel157', 'index': 1},
    }

    fixtures = {
        'date': page,
        'fixtures': {
            'Tennis': [],
            'Cricket': [],
            'Basketball': [],
            }
        }

    for line in table.findAll('tr'):
        for cl in sport_classes:
            if line.find('td', {'class': cl}) and line.find('td', {'class': cl}).contents != ['&nbsp;']:
                s = sportmapper[cl]
                if len(line.findAll('td', {'class': s['info']})) > s['index'] * 2 :
                    fixtures['fixtures'][s['name']] += [{"team":  line.find('td', {'class': cl}).text.replace("&nbsp;", " "), "school": line.findAll('td', {'class': s['school']})[s['index']].text.replace("&nbsp;", " "), "location": line.findAll('td', {'class': s['info']})[s['index']].text.replace("&nbsp;", " "), "time": line.findAll('td', {'class': s['info']})[s['index'] + 1].text.replace("&nbsp;", " ")}]

    return fixtures

class Command(NoArgsCommand):
    help = "Grab All Fixtures And Push Them In The DB"

    def handle_noargs(self, **options):        
        index = BS(urllib2.urlopen("http://www.sydgram.nsw.edu.au/co-curricular/sport/fixtures/"))
        f = grabFixtures(str(index.find('h1', text="Sports Fixtures").next.next.a['href']))
        for sport in f['fixtures']:
            s = Sport.objects.get(name=sport)
            for fixture in f['fixtures'][sport]:
                t = Team.objects.get(sport=s, name=fixture['team'])
                f = Fixture(
                    team = t,
                    time = fixture['time'],
                    location = fixture['location'],
                    date = f['date'],
                    )
                f.save()


