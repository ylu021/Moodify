import json
import os
import tweepy

# source .env && python tweets.py
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

def get_live_twitter_feed():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    user = api.get_user('AndrewYNg')
    timeline = api.user_timeline(screen_name = 'AndrewYNg', count = 100, include_rts = False)
    # timeline = user.timeline
    # print dir(timeline)

    api_info = []
    for status in timeline: #not iterateble
        status_info = {
            "text": status.text
        }
        api_info.append(status_info)

    return api_info


def save_twitter_feed(feed):
    with open("feed_cache.json", "w") as f:
        f.write(json.dumps(feed))


def get_cached_twitter_feed():
    with open("feed_cache.json", "r") as f:
        return json.loads(f.read())


def generate_cache():
    twitter_feed = get_live_twitter_feed()
    save_twitter_feed(twitter_feed)


if __name__ == '__main__':
    # generate_cache()
    print get_cached_twitter_feed()
    # get_live_twitter_feed()