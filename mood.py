import httplib, urllib, base64, json


def get_strongest_emotion(raw_result):
    """
        Returns:
            The strongest emotion in image or if there's multiple faces a list representing
                strongest emotion in each face is returned.
    """

    num_faces, res = len(raw_result), raw_result
    # print(res[0])
    # print(num_faces)
    if num_faces < 1:
        return None
    elif num_faces == 1:
        return max(res[0]['scores'], key=(lambda s: res[0]['scores'][s]))
    else:
        return [max(face['scores'], key=(lambda s: face['scores'][s])) for face in res]


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '6efa889bfbe148baa9fa5782e2747ba8',
}

params = urllib.urlencode({
})

#hard-coded images
arr = [
    'http://i.dailymail.co.uk/i/pix/2014/01/09/article-2536579-1A86E6E100000578-463_634x626.jpg',
    'http://img2.timeinc.net/people/i/2016/news/160208/taylor-swift-01-435.jpg',
    'https://s-media-cache-ak0.pinimg.com/236x/70/1f/8b/701f8b05ff6a8a3cd8db3ded83a748f6.jpg',
    'http://sev.h-cdn.co/assets/15/09/1424899427-rs_600x800-150225111050-b-nxvsqwkaari6_.jpg',
    'http://media.cmgdigital.com/shared/lt/lt_cache/aresize/835x529/img/photos/2016/05/28/d2/68/Taylor_Swift_cat_selfie.PNG',
    'https://i.ytimg.com/vi/3oKucp489qc/hqdefault.jpg',
    'http://static.celebuzz.com/uploads/2014/11/12/1-400x391.png',
    'https://pbs.twimg.com/media/By815U7IcAAPJdd.jpg',
    'http://67.media.tumblr.com/51d2a9e8134c497e6fd6c87b695f8b06/tumblr_n3zdnjCChE1rshsako1_500.png',
    'http://data.whicdn.com/images/230709931/large.jpg'
]

emotions = []

for item in arr:

    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, "{ 'url': '%s' }" % item, headers)
        response = conn.getresponse()
        data = response.read().decode()

        jsonresult = json.loads(data)
        # print(jsonresult)

        # print(get_strongest_emotion(jsonresult))
        emotions.append(get_strongest_emotion(jsonresult))

        conn.close()
    except Exception as e:
        print("[Errno {0}]".format(e))

def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o

def findMax(list):
    from collections import Counter
    cnt = Counter(list)
    return cnt.most_common(1)

#overall emotion
def exportEmotion():
    return findMax(list(traverse(emotions)))[0][0]

