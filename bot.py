import tweepy, time, sys


CONSUMER_KEY = 'KoPMGw0HQ5djvqoxTLgpHM2Zw'
CONSUMER_SECRET = 'pIUBvkrwOY56omfAtEHCF0vyX9oAGYD6ZyBIWNLJx1E7FgBsAo'
ACCESS_KEY = '1045818477133451265-fIUpfDPW3vfLsO8IwZjYcriPeqcL0b'
ACCESS_SECRET = 'sFOywZb2l92wQeCCBYrVIB39SJhuKIPzHj1cu6V3nYjg2'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("test tweet")