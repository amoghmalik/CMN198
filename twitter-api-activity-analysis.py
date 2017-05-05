# Written by Joel Fischbein
#email account : cmn198twitterbot@gmail.com
#email password: sentiment

from __future__ import print_function
import twitter

CONSUMER_KEY = 'sYdoXdwc2pa1gU5OGRB5aaxXV'
CONSUMER_SECRET = 'zVCdZyZY5bRzDmXuM9Uu4r6EHonxTonJpbLXA4I4Pzitno3JGM'
ACCESS_TOKEN = '857071999100768256-LkWoPQXfC5Yo1j88sylTAHVGNQ6iXeO'
ACCESS_TOKEN_SECRET = '2CGKePsPEgGYDjdjaydE1LppSOjNt4FFHtluXbKPRd5WK'


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

if __name__ == '__main__':
    userSuggestCategories = api.GetUserSuggestionCategories()
    userSuggests = []
    for cat in userSuggestCategories:
        userSuggests.append(api.GetUserSuggestion(cat))
    print([user.name for user in userSuggests])