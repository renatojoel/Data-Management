import tweepy #import the tweepy library to be able to use it
import json #import the json library

client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAEMl7wEAAAAA5Kj8xnSmNJgqSxYtpK5pnarEVh0%3DbGsSdmqMhgSqTYSJKTKbuHguFlbsc6TLO01qhtQ2br4ch4n0LS"
)

#The Twitter API client is initialised using a Bearer Token, which identifies the developer 
#and grants access to the Twitter API endpoints that do not require user-level authentication.

query = "#Debt -is:retweet"
#The query string is defined to search for tweets containing the hashtag #Debt, 
#while excluding retweets to ensure only original content is collected.

tweets = []
#An empty list is created to store the tweet data extracted from the API response.

response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["created_at", "text", "author_id", "lang"]
)

#A request is made to the Twitter API to retrieve recent tweets that match the query. 
#The request specifies the maximum number of tweets to return and the tweet fields to include.

if response.data:
    for tweet in response.data:
        tweets.append(tweet.data)

#If the API returns tweet data, each tweet object is converted into a dictionary
#and appended to the list that will later be saved to a JSON file.


with open("Debt.json", "w", encoding="utf-8") as f:
    json.dump(tweets, f, indent=4, ensure_ascii=False)
#A JSON file is created (or overwritten) to store the collected tweets. 
#The file is encoded in UTF-8 and formatted with indentation for readability.

print("TWEETS SAVED SUCCESSFULLY!") #A confirmation message is printed to indicate that the process completed successfully.