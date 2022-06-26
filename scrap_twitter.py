import tweepy
import json
import pandas as pd
query = "flipkart"
access_token = "1434236502779654145-Px1uZyiMlEsueD3RZtiSGx6UZDqq6k"
access_token_secret = "GQ6OBMDkhJLNACVu1oLgsimwZPs8GncZVEsVKOraejaXt"
consumer_key = "BmnxYKixZQ9gMKb7Quy3vooQe"
consumer_key_secret = "ipYK5UI6iJvGKSxyXzKVsxXuxrIvY7XwXBdBolsduFsnwXOnbZ"

auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)




# number_of_tweets = 200
# likes= []
# tweets = []
# time = []
tweets = tweepy.Cursor(api.search_tweets,q=query,count=100,tweet_mode= 'extended').items(1)

# for i in tweepy.Cursor(api.search,q="flipkart",tweet_mode= "extended").items(number_of_tweets):
#     tweets.append(i.full_text)
#     likes.append(i.favorite_count)
#     time.append(i.created_at)

for tweet in tweets:
    print(tweet.full_text)

# df = pd.DataFrame({'tweets':tweets,'likes':likes,'time':time})