import tweepy, time, random
from config import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY, ACCESS_SECRET
from apscheduler.schedulers.blocking import BlockingScheduler


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def getQuote():
    line = random.randint(0,758)
    file = open("quotes.txt",'r')
    content = file.readlines()
    return(content[line])
    file.close()

def tweetQuote():
    api.update_status(getQuote())

scheduler = BlockingScheduler()
scheduler.add_job(tweetQuote, 'interval', hours=4)
scheduler.start()