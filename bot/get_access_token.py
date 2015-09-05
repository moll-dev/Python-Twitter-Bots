''' get_access_token.py
    
        - Gets your oauth tokens and saves them to a file

    thomas moll 2015
'''

import util

''' Put your keys here from Gabby's email '''
consumer_key = 'z3iHhHSEZk8B7qpSBplQ8OQcz'
consumer_secret = 'BFLQk18LY658SBo8yNcoXMtaJczOr95aL5sqrrW2QkcxKcR2IZ'

def main():

    # Do some OAuth Dancing
    client_token, client_secret = util.get_access_token(consumer_key, consumer_secret)

    if client_token is None or client_secret is None:
        print 'Error getting your keys, did you type your Pincode incorrectly?'
        exit()

    util.dump_keys_to_file(consumer_key, consumer_secret, client_token, client_secret)

    print '\nSuccess!'
    print 'Keys Dumped to File!'


if __name__ == '__main__':
    main()