import requests
import json
from pprint import pprint

sub_key = "68fad88873c54d92ab595cdeddd70d72"

sent_api = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
key_api = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases"

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'},
  {'id': '5', 'language': 'en', 'text': 'giant scary tree big ugly terrible'}
]}

headers   = {"Ocp-Apim-Subscription-Key": sub_key}
sentiments = requests.post(sent_api, headers=headers, json=documents)
sent = sentiments.json()['documents']
pprint(sent)
#key_phrases = requests.post(key_api, headers=headers, json=documents)
#keys = key.json()

for i in sent:
    print(str(i['score']))
