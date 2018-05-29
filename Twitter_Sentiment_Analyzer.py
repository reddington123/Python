import sys;
import tweepy;
from textblob import TextBlob;

'''
First import tweepy and TextBlob
Steps included for Twitter Sentiment Analyzer
1. Create a app on apps.twitter.com through your account.
``1.1. Customer key and Customer secret key will be automatically generated.
  1.2 Generate access token and access token secret key 
2. Get the authentication variable from OAuthHandler;  
3. Set the authentication using set_access_token;
4. Get the API using tweepy.API(auth);
5. non_bmp_map is used for characters like emoji's.
6. analysis.sentiment will give polarity and subjectivity.
7. Polarity measures how positive or negative a text is.
8. Subjectivity measures how much of a opinion it is vs how much factual it is.
'''



consumer_key='CONSUMER_KEY_HERE';
consumer_secret='CONSUMER_SECRET_HERE';

access_token='ACCESS_TOKEN_HERE';
access_token_secret='ACCESS_TOKEN_SECRET_HERE';

auth=tweepy.OAuthHandler(consumer_key,consumer_secret);
auth.set_access_token(access_token,access_token_secret);

api=tweepy.API(auth);

public_tweets=api.search('Modi');

non_bmp_map=dict.fromkeys(range(0x10000,sys.maxunicode+1),0xfffd);

for tweet in public_tweets:
    print(tweet.text.translate(non_bmp_map));
    analysis=TextBlob(tweet.text);
    print(analysis.sentiment);
