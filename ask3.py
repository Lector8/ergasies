from twython import Twython
consumer_key = 'RKimvzPos4Xo9ECWsZZT5gvvT'
consumer_secret = 'lR2QrFkc0ZPNb2kyrpwPDbIZ6RiRsHPnr2eBRrYnA5WpqMPkB8'
access_token = '831177161679724545-SOOiZhGMGQgZJtFLXgCsS2onYjKcq2v'
access_secret = '1M4xw87QMtoHBpC12wFRZK7LYP0kvvkZpBVGWIJbTLoZV'
twitter=Twython(consumer_key,consumer_secret,access_token,access_secret)
print "I'm using python to mine twitter!"
user1=raw_input("dwse onoma twitter")
a=0
for i in range(1):
	s1=twitter.get_user_timeline(screen_name="user1",count=10)
	for tweet in s1:
		s=tweet['text']
		a +=len(s.split())
user2=raw_input("dwse  onoma twitter")
b=0
for i in range(1):
    s2=twitter.get_user_timeline(screen_name="user2",count=10)
    for tweet in s2:
      s0=tweet['text']
      b +=len(s0.split()) 
if a>b:
   print user1
else:
   print user2        		
	
