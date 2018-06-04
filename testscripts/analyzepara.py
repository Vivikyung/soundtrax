from moodanalysis import moods
import requests
import json
from pprint import pprint

sub_key = "68fad88873c54d92ab595cdeddd70d72"

sent_api = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
key_api = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases"

story = """Once upon a time, there was a little girl named Goldilocks.  She  went for a walk in the forest.  Pretty soon, she came upon a house.  She knocked and, when no one answered, she walked right in.
At the table in the kitchen, there were three bowls of porridge.  Goldilocks was hungry.  She tasted the porridge from the first bowl.
'This porridge is too hot!' she exclaimed.
So, she tasted the porridge from the second bowl.
'This porridge is too cold,' she said
So, she tasted the last bowl of porridge.
'Ahhh, this porridge is just right,' she said happily and she ate it all up.
After she'd eaten the three bears' breakfasts she decided she was feeling a little tired.  So, she walked into the living room where she saw three chairs.  Goldilocks sat in the first chair to rest her feet.  
'This chair is too big!' she exclaimed.
So she sat in the second chair.
'This chair is too big, too!'  she whined.
So she tried the last and smallest chair.
'Ahhh, this chair is just right,' she sighed.  But just as she settled down into the chair to rest, it broke into pieces!
Goldilocks was very tired by this time, so she went upstairs to the bedroom.  She lay down in the first bed, but it was too hard.  Then she lay in the second bed, but it was too soft.  Then she lay down in the third bed and it was just right.  Goldilocks fell asleep.
As she was sleeping, the three bears came home.
'Someone's been eating my porridge,' growled the Papa bear.
'Someone's been eating my porridge,' said the Mama bear.
'Someone's been eating my porridge and they ate it all up!' cried the Baby bear.
'Someone's been sitting in my chair,' growled the Papa bear.
'Someone's been sitting in my chair,' said the Mama bear.
'Someone's been sitting in my chair and they've broken it all to pieces,' cried the Baby bear.
They decided to look around some more and when they got upstairs to the bedroom, Papa bear growled, 'Someone's been sleeping in my bed,'
'Someone's been sleeping in my bed, too' said the Mama bear
'Someone's been sleeping in my bed and she's still there!' exclaimed Baby bear.
Just then, Goldilocks woke up and saw the three bears.  She screamed, 'Help!'  And she jumped up and ran out of the room.  Goldilocks ran down the stairs, opened the door, and ran away into the forest.  And she never returned to the home of the three bears."""

para = story.split("\n")
queries = []
for i in range(0, len(para)):
    d = {'id': str(i)}
    d['language'] = 'en'
    d['text'] = para[i]
    queries.append(d)
full_query = { 'documents': queries }

#pprint(full_query)

headers   = {"Ocp-Apim-Subscription-Key": sub_key}
sentiments = requests.post(sent_api, headers=headers, json=full_query)
sent = sentiments.json()['documents']
pprint(sent)
#key_phrases = requests.post(key_api, headers=headers, json=full_query)
#keys = key_phrases.json()
#pprint(keys)

#for i in sent:
#    print(str(i['score']))
