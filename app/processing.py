from moodids import moodids
from moodanalysis import moodnames
import requests
import json
import time
import hashlib
import random
import urllib
from pprint import pprint

class AllMusicGuide():
    api_url = 'http://api.rovicorp.com/search/v2.1/music'

    key = '7d9vkau5knchkpa4z9pkcg7d'
    keyen = key.encode('utf-8')
    secret = 'mmj58xRfZw'
    secreten = secret.encode('utf-8')

    def _sig(self):
        timestamp = int(time.time())
        timestamp = str(timestamp).encode('utf-8')

        m = hashlib.md5()
        m.update(self.keyen)
        m.update(self.secreten)
        m.update(timestamp)

        return m.hexdigest()

    def get(self, resource, params=None):
        """Take a dict of params, and return what we get from the api"""

        if not params:
            params = {}

        params = urllib.parse.urlencode(params)

        sig = self._sig()

        url = "%s/%s?apikey=%s&sig=%s&%s" % (self.api_url, resource, self.key, sig, params)
        
        print(url)
        
        resp = requests.get(url)

        if resp.status_code != 200:
            # THROW APPROPRIATE ERROR
            pass

        return resp.json()

def analyze_file(filename):
    sub_key = "68fad88873c54d92ab595cdeddd70d72"

    sent_api = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
    key_api = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases"

    file = open(filename, "r")
    story = file.read()
    
    para = story.split("\n")
    queries = []
    for i in range(0, len(para)):
        d = {'id': str(i)}
        d['language'] = 'en'
        d['text'] = para[i]
        queries.append(d)
    full_query = { 'documents': queries }

    headers   = {"Ocp-Apim-Subscription-Key": sub_key}
    sentiments = requests.post(sent_api, headers=headers, json=full_query)
    sent = sentiments.json()['documents']

    scores = []
    for i in sent:
        scores.append(i['score'])

    print("*************************** scores! ***************************")
    pprint(scores)
    return scores

def analyze_text(story):
    sub_key = "68fad88873c54d92ab595cdeddd70d72"

    sent_api = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
    key_api = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases"
    
    para = story.split("\n")
    queries = []
    for i in range(0, len(para)):
        d = {'id': str(i)}
        d['language'] = 'en'
        d['text'] = para[i]
        queries.append(d)
    full_query = { 'documents': queries }

    headers   = {"Ocp-Apim-Subscription-Key": sub_key}
    sentiments = requests.post(sent_api, headers=headers, json=full_query)
    sent = sentiments.json()['documents']

    scores = []
    for i in sent:
        scores.append(i['score'])

    print("*************************** scores! ***************************")
    pprint(scores)
    return para, scores

def pickMoods(scores, moods):
    mood_story = []
    mood_names = []
    for s in scores:
        close = 100
        options = []
        mood = ""
        for key, value in moods.items():
            if (abs(float(value) - s) < close):
                close = abs(float(value) - s)
                mood = key
            elif (abs(float(value) - s) == close):
                options.append(key)
        if (len(options) != 0):
            options.append(mood)
            idx = random.randint(0, len(options)-1)
            mood = options[idx]
        print(mood)
        mood_story.append(mood)
        mood_names.append(moodnames[mood])
    print("*************************** MOOD IDS ***************************")
    pprint(mood_story)
    return mood_story, mood_names

def findSongs(mood):
    moodid = "moodid:" + mood
    print(moodid)
    d = { "entitytype": "song", "filter": moodid}
    a = AllMusicGuide()
    resp = a.get("filterbrowse", d)
    #songs = {}
    songs = []
    samples = []
    counter = 0
    c2 = 0
    for i in resp['searchResponse']['results']:
    #    songs[(i['song']['ids']['trackId'])] = [(i['song']['title'])]
        songtitle = (i['song']['title'])
        d2 = { "entitytype": "song", "filter": moodid, "query": songtitle, "include": "sample"}
        a2 = AllMusicGuide()
        resp2 = a2.get("search", d2)
        counter += 1
        if counter > 5:
            counter = 0
            break
        for j in resp2['searchResponse']['results']:
            if (j['song']['sample'] != '' and j['song']['sample'] != None):
                songtitle = (j['song']['title'])
                songs.append(songtitle)
                samples.append(j['song']['sample'])
            c2 += 1
            if c2 > 5:
                c2 = 0
                break
    return songs, samples

def full(story):
    parsed_text, scores = analyze_text(story)
    moods, moodnames = pickMoods(scores, moodids)
    allSongs = []
    allSamps = []
    for m in moods:
        s, samp = findSongs(m)
        allSongs.append(s)
        allSamps.append(samp)
    print(allSongs)
    return parsed_text, allSongs, allSamps, moodnames






















