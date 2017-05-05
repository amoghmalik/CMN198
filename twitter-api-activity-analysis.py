# Written by Joel Fischbein
#email account : cmn198twitterbot@gmail.com
#email password: sentiment

from __future__ import print_function
from time import sleep
import twitter


# FUNCTIONS FOR BIASING
# PostRetweet()      for retweeting
# CreateFavorite()   for liking
# CreateFriendship() for following
#   GetUsersSearch()   for acquiring users to follow
# GetSearch()        for search history biasing (ALSO RETURNS TWEETS FOR LIKING AND RETWEETING)

CONSUMER_KEY = 'sYdoXdwc2pa1gU5OGRB5aaxXV'
CONSUMER_SECRET = 'zVCdZyZY5bRzDmXuM9Uu4r6EHonxTonJpbLXA4I4Pzitno3JGM'
ACCESS_TOKEN = '857071999100768256-LkWoPQXfC5Yo1j88sylTAHVGNQ6iXeO'
ACCESS_TOKEN_SECRET = '2CGKePsPEgGYDjdjaydE1LppSOjNt4FFHtluXbKPRd5WK'

SEARCH_TERM = 'delightful'

# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

# For stalling till rate limit resets
def stall(mins):
    sleep(mins * 60)

# NEEDS TO BE TESTED
def bias_like():
    # get tweets from searched term
    tweets = api.GetSearch(term=SEARCH_TERM, count=100)
    # like all tweets
    for tweet in tweets:
        api.CreateFavorite(tweet)
    # get recommended users
    user_recs = get_rec_users()
    # unlike all tweets
    for tweet in tweets:
        api.DestroyFavorite(tweet)
    return user_recs

# NEEDS TO BE TESTED
def bias_retweet():
    # get tweets from search term
    tweets = api.GetSearch(term=SEARCH_TERM, count=100)
    # retweet them all
    for tweet in tweets:
        api.PostRetweet(tweet.id)
    # get recommended users
    user_recs = get_rec_users()

    # get retweets
    tweets = api.GetUserRetweets(count=100)
    # delete all retweets
    for tweet in tweets:
        api.DestroyStatus(tweet.id)
    return user_recs

# WORK IN PROGRESS
def bias_follow():
    # get users from search term
    users = api.GetUsersSearch(term=SEARCH_TERM, count=100)

# NEEDS TO BE TESTED
def get_rec_users():
    # get user categories
    categories = api.GetUserSuggestionCategories()
    user_suggests = []
    # user_suggests = api.GetUserSuggestion(categories[1])
    # for each (desired) category get all suggested users
    for cat in categories:
        if((cat.name != "Sports") & (cat.name != "Fashion") & (cat.name != "Gaming")):
            user_suggests.append(api.GetUserSuggestion(cat))
            # print(cat.name)
    # print([cat.name for cat in user_suggest_categories])
    return user_suggests

if __name__ == '__main__':
    print("Done")