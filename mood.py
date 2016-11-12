import http.client, urllib.request, urllib.parse, urllib.error, base64,json


def get_strongest_emotion(raw_result):
    """
        Returns:
            The strongest emotion in image or if there's multiple faces a list representing
                strongest emotion in each face is returned.
    """

    num_faces, res = len(raw_result), raw_result
    print(res[0])
    print(num_faces)
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

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, "{ \"url\": \"http://i.dailymail.co.uk/i/pix/2015/03/02/2618B90700000578-2975699-Bill_Gates_pictured_last_week_was_once_again_named_the_world_s_r-m-4_1425307530818.jpg\" }", headers)
    response = conn.getresponse()
    data = response.read().decode()

    jsonresult = json.loads(data)
    print(jsonresult)

    print(get_strongest_emotion(jsonresult))

    conn.close()
except Exception as e:
    print("[Errno {0}]".format(e))

