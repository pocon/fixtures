Notification Functions
=======================

Functions which push the data which has been passed onto them. This is where the stuff is actually broadcast out. Takes the arguments: (account, fixture object, changed).

- Account differs by notification but can be email address or pushover id or mobile #

- A fixture object has the following fields: Team, Time, Location, Date.

- Changed is a boolean which simply shows whether the fixture has changed or not. If it's false, that means this notification hasn't been sent out yet (Thursday nights). If it's true, this is more urgent as it means a game has been cancelled or something, so you should highlight the fact it has been changed in the message.


Functions:

## send_pushover ##

Send Message along the lines of:

16A Cricket Fixture on 2 SEP 12 is at Weigall 3 at 6:00 AM.

or:

UPDATE: 16A Cricket Fixture on 2 SEP 12 is at Weigall 3 at 12:00 AM.

Most important, send with the very simple function from: https://github.com/laprice/pushover :

    def send_message(account, message):
    	# mild sanity check on the message
    	if len(message) > 512:
           sys.exit("message too big")
    	payload = {
      	         'token': <api key>,
     		 'user' : <account>,
    		 'message': message,
    		 }
	r = requests.post('https://api.pushover.net/1/messages.json', data=payload )
    	if not r.status_code == requests.codes.ok:
           print r.headers

API Key: PysFgueSijmkzZEL3MSZkG2f9yxMtj

## send_email ##

Quite easy: https://docs.djangoproject.com/en/dev/topics/email/

Put in any from address for the moment, in future, a real one shall be put in.

## send_sms ##

Extension, but would be awesome. Use Twilio. Good documentation at: https://github.com/twilio/twilio-python