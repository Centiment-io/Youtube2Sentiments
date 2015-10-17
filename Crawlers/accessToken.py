import webbrowser
import tweepy
import keys

"""
    Query the user for their consumer key/secret
    then attempt to fetch a valid access token.
    Utility Script to get access tokens
"""

if __name__ == "__main__":

    #consumer_key = raw_input('Consumer key: ').strip()
    #consumer_secret = raw_input('Consumer secret: ').strip()
    consumer_key = keys.ckey
    consumer_secret = keys.csecret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Open authorization URL in browser
    webbrowser.open(auth.get_authorization_url())

    # Ask user for verifier pin
    pin = raw_input('Verification pin number from twitter.com: ').strip()

    # Get access token
    token = auth.get_access_token(verifier=pin)

    # Give user the access token
    print 'Access token:'
    print '  Key: %s' % token.key
    print '  Secret: %s' % token.secret