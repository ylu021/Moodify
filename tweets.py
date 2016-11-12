import tweepy

auth = tweepy.OAuthHandler('XUKst9fg5F3wJ8SSK1XhAKnYe', 'mIZVZ4aC9X1f5gt5cb6zWE9e3xsCJNfnVXX4fflneuOGdIfTcx')
auth.set_access_token('3007796788-F6ACL5eP4ulPyOvBq42ic7TLJ1JsSca9r95N2W6', 'u6bFzwrJuukl3Kpsf3mCQwMTCd2wxVAc34gXcZHwXQctr')

api = tweepy.API(auth)

user = api.get_user('AndrewYNg')

print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name