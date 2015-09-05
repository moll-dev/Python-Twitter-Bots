#!/usr/bin/env python
#
# Copyright 2007-2013 The Python-Twitter Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webbrowser
from requests_oauthlib import OAuth1Session

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'

def get_access_token(consumer_key, consumer_secret):
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
    except ValueError, e:
        print 'Invalid respond from Twitter requesting temp token: %s' % e
        return None, None

    url = oauth_client.authorization_url(AUTHORIZATION_URL)

    print ''
    print 'Trying to open the authorization url, be patient!'
    print 'if a browser will not start, copy the URL to your browser'
    print ''
    print url
    print ''

    webbrowser.open(url)
    print 'After you authorize this app to use your twitter account, please'
    print 'type the pincode below\n'
    pincode = raw_input('Pincode? : ')

    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
                                 resource_owner_key=resp.get('oauth_token'),
                                 resource_owner_secret=resp.get('oauth_token_secret'),
                                 verifier=pincode
    )
    try:
        resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
    except ValueError, e:
        print 'Invalid respond from Twitter requesting access token: %s' % e
        return None, None

    return resp.get('oauth_token'), resp.get('oauth_token_secret')

def dump_keys_to_file(consumer_key, consumer_secret, client_token, client_secret):
    # WARNING DON'T MODIFY 'secrets.py' ITS IN THE GIT IGNORE FOR A REASON!!!!
    with open('secrets.py', 'w') as outfile:
        key_dict = { 'consumer_key'    : consumer_key, 
                     'consumer_secret' : consumer_secret,
                     'client_token'    : client_token,
                     'client_secret'   : client_secret}

        outfile.write('keys = {\n')
        for value in key_dict:
            outfile.write('\t\''+value+'\' : \''+str(key_dict[value])+'\',\n')
        outfile.write('}')

def main():
    consumer_key = raw_input('Enter your consumer key: ')
    consumer_secret = raw_input("Enter your consumer secret: ")
    get_access_token(consumer_key, consumer_secret)


if __name__ == "__main__":
    main()