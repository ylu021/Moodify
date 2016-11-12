import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '4b973b799e844edc9c5db60005339386',
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
    }
  ]
}

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(obj), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))