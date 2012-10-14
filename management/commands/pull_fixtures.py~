"""
A management command which Grabs MPs Twitter handles from OA

"""

from django.core.management.base import NoArgsCommand
from members.models import *
from BeautifulSoup import BeautifulStoneSoup as BS
import urllib2

class Command(NoArgsCommand):
    help = "Grab All Members Twitter and Add them Into the DB"

    def handle_noargs(self, **options):        
        page = BS(urllib2.urlopen("http://data.openaustralia.org/members/twitter.xml"))

        for member in page.findAll("personinfo"):
            m = Member.objects.get(oa_id=member['id'])
            try:
                m.twitter = member['mp_twitter_screen_name']
            except KeyError:
                pass

            m.save()


