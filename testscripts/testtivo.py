import requests # http://pypi.python.org/pypi/requests
import time
import hashlib
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

if __name__ == "__main__":
    d = { "entitytype": "song", "filter": "moodid:XA0000000694"}
    a = AllMusicGuide()
    resp = a.get("filterbrowse", d)
    songs = {}
    for i in resp['searchResponse']['results']:
        songs[(i['song']['ids']['trackId'])] = [(i['song']['title'])]
    
    pprint(songs)
