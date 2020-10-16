import tweepy

auth = tweepy.OAuthHandler("XaEQo6vfMbEIZsPjFNnmm4kB8", "v1xYfum8kWUVqz6iO6aTX7gFJnd7wfhHLtaKUoqie551aCrgZX")
auth.set_access_token("375259383-N8N1XlbuvwCZeJEihALTvgjlCWatwgrnlkI2aNHj", "yRuBlEWc5Gr9JUGFAnOen7oEbUILZ18OOAnUEgklXneBH")

#pip install -U textblob-de

  #import nltk
  #nltk.download('punkt')

from textblob_de import TextBlobDE as TextBlob #2
text1 = '''Das ist alles wunderschön. Ich freue mich.''' #3`
text2 = '''Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag. Ich muss unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen. Aber leider habe ich nur noch EUR 3,50 in meiner Brieftasche.''' #4
text3 = '''Es ist so schlimm und so furchtbar. Es war alles so traurig und grässlich.''' #5
blob = TextBlob(text1) #6
print(blob.sentences) #7
print(blob.tokens) #8
print(blob.tags) #9
print(blob.noun_phrases) #10
print(blob.sentiment) #11
blob = TextBlob(text2) #12
print(blob.sentiment) #13
print(blob.sentiment.polarity)

#Quelle: https://machine-learning-blog.de/2019/06/03/stimmungsanalyse-sentiment-analysis-auf-deutsch-mit-python/

#!pip install jsonpickle
import time
import sys
import jsonpickle
import os
api = tweepy.API(auth)

totalpolarity = 0
nopostweets = 0
searchQuery = "\"John Carney\" OR \"Julianne Murray\" OR \"Eric Holcomb\" OR \"Woody Myers\" OR \"Donald Rainwater\" OR \"Mike Parson\" OR \"Nicole Galloway\" OR \"Mike Cooney\" OR \"Greg Gianforte\" OR \"Chris Sununu\" " #OR \"Dan Feltes\" OR \"Roy Cooper\" OR \"Dan Forest\" OR \"Doug Burgum\" OR \"Shelley Lenz\" OR \"Spencer Cox\" OR \"Christopher Peterson\" OR \"Phil Scott\" OR \"David Zuckerman\" OR \"Jay Inslee\" OR \"Loren Culp\" OR \"Jim Justice\" OR \"Ben Salango\" OR \"Daniel Luz\" "  # this is what we\"re searching for 
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = '/Volumes/TOSHIBA/tweetsgov201010.txt' # We'll store the tweets in a text file.
sin = "2020-10-10"
til = "2020-10-11"


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang="en", tweet_mode='extended', since=sin, until=til)
                    time.sleep(5)
                    for elem in new_tweets:
                          blob = TextBlob(elem.full_text)
                          totalpolarity = totalpolarity + blob.sentiment.polarity
                          try:
                            print("RETWEETED TWEET")
                            print(elem.retweeted_status.full_text)
                            print("from")
                            print(elem.user.location)
                            print("---------------------")
                            if ("Deutschland" in elem.retweeted_status.user.location) or ("Deutschland" in elem.user.location):
                              nopostweets = nopostweets + 1

                          except AttributeError: 
                            print(elem.full_text)
                            print("from")
                            print(elem.user.location)
                            print("---------------------")
                            if "Deutschland" in elem.user.location:
                              nopostweets = nopostweets + 1
                else:
                    time.sleep(5)
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId, lang="en", tweet_mode='extended', since=sin, until=til)
                    for elem in new_tweets:
                          blob = TextBlob(elem.full_text)
                          totalpolarity = totalpolarity + blob.sentiment.polarity
                          try:
                            if ("Deutschland" in elem.retweeted_status.user.location) or ("Deutschland" in elem.user.location):
                              nopostweets = nopostweets + 1
                          except AttributeError: 
                            if "Deutschland" in elem.user.location:
                              nopostweets = nopostweets + 1
            else:
                if (not sinceId):
                    time.sleep(5)
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),lang="en",tweet_mode='extended', since=sin, until=til)
                    for elem in new_tweets:
                          blob = TextBlob(elem.full_text)
                          totalpolarity = totalpolarity + blob.sentiment.polarity
                          try:
                            if ("Deutschland" in elem.retweeted_status.user.location) or ("Deutschland" in elem.user.location):
                              nopostweets = nopostweets + 1
                          except AttributeError: 
                            if "Deutschland" in elem.user.location:
                              nopostweets = nopostweets + 1
                else:
                    time.sleep(5)
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId,lang="en",tweet_mode='extended',since=sin, until=til)
                    for elem in new_tweets:
                          blob = TextBlob(elem.full_text)
                          totalpolarity = totalpolarity + blob.sentiment.polarity
                          try:
                            if ("Deutschland" in elem.retweeted_status.user.location) or ("Deutschland" in elem.user.location):
                              nopostweets = nopostweets + 1
                          except AttributeError: 
                            if "Deutschland" in elem.user.location:
                              nopostweets = nopostweets + 1
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break
 

# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
    sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = -1
    searchQuery = "\"Dan Feltes\" OR \"Roy Cooper\" OR \"Dan Forest\" OR \"Doug Burgum\" OR \"Shelley Lenz\" OR \"Spencer Cox\" OR \"Christopher Peterson\" OR \"Phil Scott\" OR \"David Zuckerman\" OR \"Jay Inslee\" OR \"Loren Culp\" OR \"Jim Justice\" OR \"Ben Salango\" OR \"Daniel Luz\" "  # this is what we\"re searching for 

    print("Downloading max {0} tweets".format(maxTweets))
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang="en", tweet_mode='extended', since=sin, until=til)
                    time.sleep(5)
                    for elem in new_tweets:
                          blob = TextBlob(elem.full_text)
                          totalpolarity = totalpolarity + blob.sentiment.polarity
                          try:
                            print("RETWEETED TWEET")
                            print(elem.retweeted_status.full_text)
                            print("from")
                            print(elem.user.location)
                            print("---------------------")
                            if ("Deutschland" in elem.retweeted_status.user.location) or ("Deutschland" in elem.user.location):
                              nopostweets = nopostweets + 1

                          except AttributeError: 
                            print(elem.full_text)
                            print("from")
                            print(elem.user.location)
                            print("---------------------")
                            if "Deutschland" in elem.user.location:
                              nopostweets = nopostweets + 1
                else:
                    time.sleep(5)
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId, lang="en", tweet_mode='extended', since=sin, until=til)
                    for elem in new_tweets:
                          blob = TextBlob(elem.full_text)
                          totalpolarity = totalpolarity + blob.sentiment.polarity
                          try:
                            if ("Deutschland" in elem.retweeted_status.user.location) or ("Deutschland" in elem.user.location):
                              nopostweets = nopostweets + 1
                          except AttributeError: 
                            if "Deutschland" in elem.user.location:
                              nopostweets = nopostweets + 1
            else:
                if (not sinceId):
                    time.sleep(5)
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),lang="en",tweet_mode='extended', since=sin, until=til)
                    for elem in new_tweets:
                          blob = TextBlob(elem.full_text)
                          totalpolarity = totalpolarity + blob.sentiment.polarity
                          try:
                            if ("Deutschland" in elem.retweeted_status.user.location) or ("Deutschland" in elem.user.location):
                              nopostweets = nopostweets + 1
                          except AttributeError: 
                            if "Deutschland" in elem.user.location:
                              nopostweets = nopostweets + 1
                else:
                    time.sleep(5)
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId,lang="en",tweet_mode='extended',since=sin, until=til)
                    for elem in new_tweets:
                          blob = TextBlob(elem.full_text)
                          totalpolarity = totalpolarity + blob.sentiment.polarity
                          try:
                            if ("Deutschland" in elem.retweeted_status.user.location) or ("Deutschland" in elem.user.location):
                              nopostweets = nopostweets + 1
                          except AttributeError: 
                            if "Deutschland" in elem.user.location:
                              nopostweets = nopostweets + 1
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break


print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
print(totalpolarity)
print("Tweets aus Deutschland:")
print(nopostweets)
