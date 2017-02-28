import time
import tweepy
from tweepy import OAuthHandler

consumer_key = 'RKimvzPos4Xo9ECWsZZT5gvvT'
consumer_secret = 'lR2QrFkc0ZPNb2kyrpwPDbIZ6RiRsHPnr2eBRrYnA5WpqMPkB8'
access_token = '831177161679724545-SOOiZhGMGQgZJtFLXgCsS2onYjKcq2v'
access_secret = '1M4xw87QMtoHBpC12wFRZK7LYP0kvvkZpBVGWIJbTLoZV'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
print "I'm using python to mine twitter!"
user1=raw_input("dwse onoma twitter")
sleeptime=4
pages=tweepy.Cursor(api.followers,screen_name="user1").pages()
a=[]
while True:
	try:
		page=next(pages)
		time.sleep(sleeptime)
	except tweepy.TweepError:
	    time.sleep(60*15)
	    page=next(pages)
	except StopIteration:
	    break
	for user in page:
	    a.extend(user.screen_name)
user2=raw_input("dwse onoma twitter")
pages1=tweepy.Cursor(api.followers,screen_name="user2").pages()
while True:
    try:
       page1=next(pages1)
       time.sleep(sleeptime)
    except tweepy.TweepError:
       time.sleep(60*15)
       page1=next(pages1)
    except StopIteration:
       break
    for user3 in page1:
       a.extend(user3.screen_name)
commonfl=[]
seen=set()
for x in a:
    if x not in seen:
       commonfl.append(x)
       seen.add(x)
print commonfl              


		


	    



	        	
       	