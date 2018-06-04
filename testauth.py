from pprint import pprint
import requests

def find_track(trackname):
    api_url = "http://api.7digital.com/1.2/track/search?"
    auth_key = "7d4vr6cgb392"
    headers = {"q": trackname, "shopId": "2020", "oauth_consumer_key": auth_key, "usageTypes": "adsupportedstreaming​"}
    trackID = requests.get(api_url, headers=headers)
    track = trackID.json().encode('utf-8')
    pprint(track)

if __name__ == "__main__":
    find_track("happy")
