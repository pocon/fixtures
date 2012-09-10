Scraper
==========

Use BeautifulSoup:

http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html

Examples of scrapers can be found under another project of mine:

https://github.com/pocon/Politika/tree/master/members/management/commands

Two Scrapers (Implemented as functions):

## get_teams ##

Function which just returns a dictionary of sports with list of all the teams that exist in that sport. EG:
	
	return {'tennis': ['13A', '13B'], 'rowing': ['1st XIII']}

## get_fixtures ##

Same as above in format but instead of just teams, returns their fixtures as well, implemented as a nested list in the form {'sport': [['team', 'time', 'location']]}. Also has an entry to the dictionary: {'date': 'date'}, where date is the string from the top of the table. EG:
	
	return {'date': '3 SEP 12', 'tennis': [['13A', '12:00', 'Weigall 2'], ['13B', '1:00', 'Weigall 3']]}

