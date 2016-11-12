import httplib, urllib, base64, json, os
from tweets import get_cached_twitter_feed

TEXTANALYSIS_API_KEY = os.getenv("TEXTANALYSIS_API_KEY")

# source .env && python sentiment.py

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': TEXTANALYSIS_API_KEY,
}

params = urllib.urlencode({
    # Request parameters
    'numberOfLanguagesToDetect':  1,
})

obj = {
  "documents": [
    {
      "language": "en",
      "id": "string",
      "text": "hello world"
    },
    {
      "language": "en",
      "id": "string2",
      "text": "sad"
    }
  ]
}

# create json object
obj = {}
obj["documents"] = []
# status = []

count = 0
for tweets in get_cached_twitter_feed():
  temp = {}
  temp["language"] = "en"
  temp["id"] = "id"+str(count)
  temp["text"] = tweets["text"].encode('utf-8')
  obj["documents"].append(temp) #create a documents
  count = count+1

# print obj["documents"]
score = []

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(json.dumps(obj)), headers)
    response = conn.getresponse()
    data = response.read()
    for singlefeed in json.loads(data)["documents"]:
      score.append(singlefeed["score"])
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

print sum(score)/len(score)