''' check_authentication.py

	- Simple check to see if everything is working!

	thomas moll 2015
'''

import twitter
from secrets import keys

api = twitter.Api(keys['consumer_key'], keys['consumer_secret'],
                  keys['client_token'], keys['client_secret'])

try:
	user = api.VerifyCredentials()
	print '\nHello there,',user.name.encode('utf-8'),'from',user.location.encode('utf-8')
	print 'You have successfully authorized your twitter account!'
	print 'You\'re all ready to move to the next step and start making a bot!'

except Exception, e:
	print 'Something went wrong :(\nTry working through the setup steps again.'
	print e
