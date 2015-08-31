'''
    Twitter Bot Skeleton 
    Use this to get started making your very own Rad Twitter Bot
'''

#Import the Twitter API 
import twitter

'''
    Gets our keys from a file
    Parameters: 
        filename - given filename to read keys from 
    Returns: 
        keys - a dictionary of keys to OAuth with Twitter 
'''
def getKeysFromFile(filename):
    f = open(filename, "r")
    keys_array = f.read().split('\n')

    keys = {'consumer_key':keys_array[0], 'consumer_secret':keys_array[1], 'access_token_key':keys_array[2], 'access_token_secret':keys_array[3]}

    return keys

keys = getKeysFromFile('keys.txt')
api = twitter.Api(keys['consumer_key'], keys['consumer_secret'],
                  keys['access_token_key'], keys['access_token_secret'])

'''
    Method to verify that your keys work
'''
def verifyCredentials():
     print api.VerifyCredentials()

'''
    Method to post a status, deletes any duplicates 
    Parameters: 
        status - given status to post to Twitter 
    Returns: 
        The result of the PostUpdate API call. 
'''
def postStatus(status): 
    feed = api.GetUserTimeline()

    for tweet in feed: 
        if status == tweet.text: 
            api.DestroyStatus(tweet.id)
    return api.PostUpdate(status, None)


'''
    A few recipes to help you get started
'''

'''
    Method to delete a tweet with a specific word. 
    This method will ignore the case of the word. 
    Parameters: 
        word - the word to be deleted 
'''
def deleteTweet(word): 
    word = word.lower()
    print "Looking for " + "\'" + word + "\'" + "!"
    feed = api.GetUserTimeline()
    for tweet in feed: 
        if word in tweet.text.lower(): 
            print "deleting tweet..."
            api.DestroyStatus(tweet.id)
        else: 
            print "word not found!"

#postStatus("Twitter Bot test!")
deleteTweet('Bot')
