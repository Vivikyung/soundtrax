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
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
]}

moods = {'documents' : [
    {'id': '1', 'language': 'en', 'text': 'Acerbic'},
    {'id': '2', 'language': 'en', 'text': 'Aggressive'},
    {'id': '3', 'language': 'en', 'text': 'Agreeable'},
    {'id': '4', 'language': 'en', 'text': 'Airy'},
    {'id': '5', 'language': 'en', 'text': 'Ambitious'},
    {'id': '6', 'language': 'en', 'text': 'Amiable/Good-Natured'},
    {'id': '7', 'language': 'en', 'text': 'Angry'},
    {'id': '8', 'language': 'en', 'text': 'Angst-Ridden'},
    {'id': '9', 'language': 'en', 'text': 'Anguished/Distraught'},
    {'id': '10', 'language': 'en', 'text': 'Angular'},
    {'id': '11', 'language': 'en', 'text': 'Animated'},
    {'id': '12', 'language': 'en', 'text': 'Apocalyptic'},
    {'id': '13', 'language': 'en', 'text': 'Arid'},
    {'id': '14', 'language': 'en', 'text': 'Athletic'},
    {'id': '15', 'language': 'en', 'text': 'Atmospheric'},
    {'id': '16', 'language': 'en', 'text': 'Austere'},
    {'id': '17', 'language': 'en', 'text': 'Autumnal'},
    {'id': '18', 'language': 'en', 'text': 'Belligerent'},
    {'id': '19', 'language': 'en', 'text': 'Benevolent'},
    {'id': '20', 'language': 'en', 'text': 'Bitter'},
    {'id': '21', 'language': 'en', 'text': 'Bittersweet'},
    {'id': '22', 'language': 'en', 'text': 'Bleak'},
    {'id': '23', 'language': 'en', 'text': 'Boisterous'},
    {'id': '24', 'language': 'en', 'text': 'Bombastic'},
    {'id': '25', 'language': 'en', 'text': 'Brash'},
    {'id': '26', 'language': 'en', 'text': 'Brassy'},
    {'id': '27', 'language': 'en', 'text': 'Bravado'},
    {'id': '28', 'language': 'en', 'text': 'Bright'},
    {'id': '29', 'language': 'en', 'text': 'Brittle'},
    {'id': '30', 'language': 'en', 'text': 'Brooding'},
    {'id': '31', 'language': 'en', 'text': 'Calm/Peaceful'},
    {'id': '32', 'language': 'en', 'text': 'Campy'},
    {'id': '33', 'language': 'en', 'text': 'Capricious'},
    {'id': '34', 'language': 'en', 'text': 'Carefree'},
    {'id': '35', 'language': 'en', 'text': 'Cartoonish'},
    {'id': '36', 'language': 'en', 'text': 'Cathartic'},
    {'id': '37', 'language': 'en', 'text': 'Celebratory'},
    {'id': '38', 'language': 'en', 'text': 'Cerebral'},
    {'id': '39', 'language': 'en', 'text': 'Cheerful'},
    {'id': '40', 'language': 'en', 'text': 'Child-like'},
    {'id': '41', 'language': 'en', 'text': 'Circular'},
    {'id': '42', 'language': 'en', 'text': 'Clinical'},
    {'id': '43', 'language': 'en', 'text': 'Cold'},
    {'id': '44', 'language': 'en', 'text': 'Comic'},
    {'id': '45', 'language': 'en', 'text': 'Complex'},
    {'id': '46', 'language': 'en', 'text': 'Concise'},
    {'id': '47', 'language': 'en', 'text': 'Confident'},
    {'id': '48', 'language': 'en', 'text': 'Confrontational'},
    {'id': '49', 'language': 'en', 'text': 'Cosmopolitan'},
    {'id': '50', 'language': 'en', 'text': 'Crunchy'},
    {'id': '51', 'language': 'en', 'text': 'Cynical/Sarcastic'},
    {'id': '52', 'language': 'en', 'text': 'Dark'},
    {'id': '53', 'language': 'en', 'text': 'Declamatory'},
    {'id': '54', 'language': 'en', 'text': 'Defiant'},
    {'id': '55', 'language': 'en', 'text': 'Delicate'},
    {'id': '56', 'language': 'en', 'text': 'Demonic'},
    {'id': '57', 'language': 'en', 'text': 'Desperate'},
    {'id': '58', 'language': 'en', 'text': 'Detached'},
    {'id': '59', 'language': 'en', 'text': 'Devotional'},
    {'id': '60', 'language': 'en', 'text': 'Difficult'},
    {'id': '61', 'language': 'en', 'text': 'Dignified/Noble'},
    {'id': '62', 'language': 'en', 'text': 'Dramatic'},
    {'id': '63', 'language': 'en', 'text': 'Dreamy'},
    {'id': '64', 'language': 'en', 'text': 'Driving'},
    {'id': '65', 'language': 'en', 'text': 'Druggy'},
    {'id': '66', 'language': 'en', 'text': 'Earnest'},
    {'id': '67', 'language': 'en', 'text': 'Earthy'},
    {'id': '68', 'language': 'en', 'text': 'Ebullient'},
    {'id': '69', 'language': 'en', 'text': 'Eccentric'},
    {'id': '70', 'language': 'en', 'text': 'Ecstatic'},
    {'id': '71', 'language': 'en', 'text': 'Eerie'},
    {'id': '72', 'language': 'en', 'text': 'Effervescent'},
    {'id': '73', 'language': 'en', 'text': 'Elaborate'},
    {'id': '74', 'language': 'en', 'text': 'Elegant'},
    {'id': '75', 'language': 'en', 'text': 'Elegiac'},
    {'id': '76', 'language': 'en', 'text': 'Energetic'},
    {'id': '77', 'language': 'en', 'text': 'Enigmatic'},
    {'id': '78', 'language': 'en', 'text': 'Epic'},
    {'id': '79', 'language': 'en', 'text': 'Erotic'},
    {'id': '80', 'language': 'en', 'text': 'Ethereal'},
    {'id': '81', 'language': 'en', 'text': 'Euphoric'},
    {'id': '82', 'language': 'en', 'text': 'Exciting'},
    {'id': '83', 'language': 'en', 'text': 'Exotic'},
    {'id': '84', 'language': 'en', 'text': 'Explosive'},
    {'id': '85', 'language': 'en', 'text': 'Extroverted'},
    {'id': '86', 'language': 'en', 'text': 'Exuberant'},
    {'id': '87', 'language': 'en', 'text': 'Fantastic/Fantasy-like'},
    {'id': '88', 'language': 'en', 'text': 'Feral'},
    {'id': '89', 'language': 'en', 'text': 'Feverish'},
    {'id': '90', 'language': 'en', 'text': 'Fierce'},
    {'id': '91', 'language': 'en', 'text': 'Fiery'},
    {'id': '92', 'language': 'en', 'text': 'Flashy'},
    {'id': '93', 'language': 'en', 'text': 'Flowing'},
    {'id': '94', 'language': 'en', 'text': 'Fractured'},
    {'id': '95', 'language': 'en', 'text': 'Freewheeling'},
    {'id': '96', 'language': 'en', 'text': 'Fun'},
    {'id': '97', 'language': 'en', 'text': 'Funereal'},
    {'id': '98', 'language': 'en', 'text': 'Gentle'},
    {'id': '99', 'language': 'en', 'text': 'Giddy'},
    {'id': '100', 'language': 'en', 'text': 'Gleeful'},
    {'id': '101', 'language': 'en', 'text': 'Gloomy'},
    {'id': '102', 'language': 'en', 'text': 'Graceful'},
    {'id': '103', 'language': 'en', 'text': 'Greasy'},
    {'id': '104', 'language': 'en', 'text': 'Grim'},
    {'id': '105', 'language': 'en', 'text': 'Gritty'},
    {'id': '106', 'language': 'en', 'text': 'Gutsy'},
    {'id': '107', 'language': 'en', 'text': 'Happy'},
    {'id': '108', 'language': 'en', 'text': 'Harsh'},
    {'id': '109', 'language': 'en', 'text': 'Hedonistic'},
    {'id': '110', 'language': 'en', 'text': 'Heroic'},
    {'id': '111', 'language': 'en', 'text': 'Hostile'},
    {'id': '112', 'language': 'en', 'text': 'Humorous'},
    {'id': '113', 'language': 'en', 'text': 'Hungry'},
    {'id': '114', 'language': 'en', 'text': 'Hymn-like'},
    {'id': '115', 'language': 'en', 'text': 'Hyper'},
    {'id': '116', 'language': 'en', 'text': 'Hypnotic'},
    {'id': '117', 'language': 'en', 'text': 'Improvisatory'},
    {'id': '118', 'language': 'en', 'text': 'Indulgent'},
    {'id': '119', 'language': 'en', 'text': 'Innocent'},
    {'id': '120', 'language': 'en', 'text': 'Insular'},
    {'id': '121', 'language': 'en', 'text': 'Intense'},
    {'id': '122', 'language': 'en', 'text': 'Intimate'},
    {'id': '123', 'language': 'en', 'text': 'Introspective'},
    {'id': '124', 'language': 'en', 'text': 'Ironic'},
    {'id': '125', 'language': 'en', 'text': 'Irreverent'},
    {'id': '126', 'language': 'en', 'text': 'Jovial'},
    {'id': '127', 'language': 'en', 'text': 'Joyous'},
    {'id': '128', 'language': 'en', 'text': 'Kinetic'},
    {'id': '129', 'language': 'en', 'text': 'Knotty'},
    {'id': '130', 'language': 'en', 'text': 'Laid-Back/Mellow'},
    {'id': '131', 'language': 'en', 'text': 'Languid'},
    {'id': '132', 'language': 'en', 'text': 'Lazy'},
    {'id': '133', 'language': 'en', 'text': 'Light'},
    {'id': '134', 'language': 'en', 'text': 'Literate'},
    {'id': '135', 'language': 'en', 'text': 'Lively'},
    {'id': '136', 'language': 'en', 'text': 'Lonely'},
    {'id': '137', 'language': 'en', 'text': 'Lush'},
    {'id': '138', 'language': 'en', 'text': 'Lyrical'},
    {'id': '139', 'language': 'en', 'text': 'Macabre'},
    {'id': '140', 'language': 'en', 'text': 'Magical'},
    {'id': '141', 'language': 'en', 'text': 'Majestic'},
    {'id': '142', 'language': 'en', 'text': 'Malevolent'},
    {'id': '143', 'language': 'en', 'text': 'Manic'},
    {'id': '144', 'language': 'en', 'text': 'Marching'},
    {'id': '145', 'language': 'en', 'text': 'Martial'},
    {'id': '146', 'language': 'en', 'text': 'Meandering'},
    {'id': '147', 'language': 'en', 'text': 'Mechanical'},
    {'id': '148', 'language': 'en', 'text': 'Meditative'},
    {'id': '149', 'language': 'en', 'text': 'Melancholy'},
    {'id': '150', 'language': 'en', 'text': 'Menacing'},
    {'id': '151', 'language': 'en', 'text': 'Messy'},
    {'id': '152', 'language': 'en', 'text': 'Mighty'},
    {'id': '153', 'language': 'en', 'text': 'Monastic'},
    {'id': '154', 'language': 'en', 'text': 'Monumental'},
    {'id': '155', 'language': 'en', 'text': 'Motoric'},
    {'id': '156', 'language': 'en', 'text': 'Mysterious'},
    {'id': '157', 'language': 'en', 'text': 'Mystical'},
    {'id': '158', 'language': 'en', 'text': 'Naive'},
    {'id': '159', 'language': 'en', 'text': 'Narcotic'},
    {'id': '160', 'language': 'en', 'text': 'Narrative'},
    {'id': '161', 'language': 'en', 'text': 'Negative'},
    {'id': '162', 'language': 'en', 'text': 'Nervous/Jittery'},
    {'id': '163', 'language': 'en', 'text': 'Nihilistic'},
    {'id': '164', 'language': 'en', 'text': 'Nocturnal'},
    {'id': '165', 'language': 'en', 'text': 'Nostalgic'},
    {'id': '166', 'language': 'en', 'text': 'Ominous'},
    {'id': '167', 'language': 'en', 'text': 'Optimistic'},
    {'id': '168', 'language': 'en', 'text': 'Opulent'},
    {'id': '169', 'language': 'en', 'text': 'Organic'},
    {'id': '170', 'language': 'en', 'text': 'Ornate'},
    {'id': '171', 'language': 'en', 'text': 'Outraged'},
    {'id': '172', 'language': 'en', 'text': 'Outrageous'},
    {'id': '173', 'language': 'en', 'text': 'Paranoid'},
    {'id': '174', 'language': 'en', 'text': 'Passionate'},
    {'id': '175', 'language': 'en', 'text': 'Pastoral'},
    {'id': '176', 'language': 'en', 'text': 'Patriotic'},
    {'id': '177', 'language': 'en', 'text': 'Perky'},
    {'id': '178', 'language': 'en', 'text': 'Philosophical'},
    {'id': '179', 'language': 'en', 'text': 'Plain'},
    {'id': '180', 'language': 'en', 'text': 'Plaintive'},
    {'id': '181', 'language': 'en', 'text': 'Playful'},
    {'id': '182', 'language': 'en', 'text': 'Poignant'},
    {'id': '183', 'language': 'en', 'text': 'Positive'},
    {'id': '184', 'language': 'en', 'text': 'Powerful'},
    {'id': '185', 'language': 'en', 'text': 'Precious'},
    {'id': '186', 'language': 'en', 'text': 'Provocative'},
    {'id': '187', 'language': 'en', 'text': 'Pulsing'},
    {'id': '188', 'language': 'en', 'text': 'Pure'},
    {'id': '189', 'language': 'en', 'text': 'Quirky'},
    {'id': '190', 'language': 'en', 'text': 'Rambunctious'},
    {'id': '191', 'language': 'en', 'text': 'Ramshackle'},
    {'id': '192', 'language': 'en', 'text': 'Raucous'},
    {'id': '193', 'language': 'en', 'text': 'Reassuring/Consoling'},
    {'id': '194', 'language': 'en', 'text': 'Rebellious'},
    {'id': '195', 'language': 'en', 'text': 'Reckless'},
    {'id': '196', 'language': 'en', 'text': 'Refined'},
    {'id': '197', 'language': 'en', 'text': 'Reflective'},
    {'id': '198', 'language': 'en', 'text': 'Regretful'},
    {'id': '199', 'language': 'en', 'text': 'Relaxed'},
    {'id': '200', 'language': 'en', 'text': 'Reserved'},
    {'id': '201', 'language': 'en', 'text': 'Resolute'},
    {'id': '202', 'language': 'en', 'text': 'Restrained'},
    {'id': '203', 'language': 'en', 'text': 'Reverent'},
    {'id': '204', 'language': 'en', 'text': 'Rhapsodic'},
    {'id': '205', 'language': 'en', 'text': 'Rollicking'},
    {'id': '206', 'language': 'en', 'text': 'Romantic'},
    {'id': '207', 'language': 'en', 'text': 'Rousing'},
    {'id': '208', 'language': 'en', 'text': 'Rowdy'},
    {'id': '209', 'language': 'en', 'text': 'Rustic'},
    {'id': '210', 'language': 'en', 'text': 'Sacred'},
    {'id': '211', 'language': 'en', 'text': 'Sad'},
    {'id': '212', 'language': 'en', 'text': 'Sarcastic'},
    {'id': '213', 'language': 'en', 'text': 'Sardonic'},
    {'id': '214', 'language': 'en', 'text': 'Satirical'},
    {'id': '215', 'language': 'en', 'text': 'Savage'},
    {'id': '216', 'language': 'en', 'text': 'Scary'},
    {'id': '217', 'language': 'en', 'text': 'Scattered'},
    {'id': '218', 'language': 'en', 'text': 'Searching'},
    {'id': '219', 'language': 'en', 'text': 'Self-Conscious'},
    {'id': '220', 'language': 'en', 'text': 'Sensual'},
    {'id': '221', 'language': 'en', 'text': 'Sentimental'},
    {'id': '222', 'language': 'en', 'text': 'Serious'},
    {'id': '223', 'language': 'en', 'text': 'Severe'},
    {'id': '224', 'language': 'en', 'text': 'Sexual'},
    {'id': '225', 'language': 'en', 'text': 'Sexy'},
    {'id': '226', 'language': 'en', 'text': 'Shimmering'},
    {'id': '227', 'language': 'en', 'text': 'Silly'},
    {'id': '228', 'language': 'en', 'text': 'Sleazy'},
    {'id': '229', 'language': 'en', 'text': 'Slick'},
    {'id': '230', 'language': 'en', 'text': 'Smooth'},
    {'id': '231', 'language': 'en', 'text': 'Snide'},
    {'id': '232', 'language': 'en', 'text': 'Soft/Quiet'},
    {'id': '233', 'language': 'en', 'text': 'Somber'},
    {'id': '234', 'language': 'en', 'text': 'Soothing'},
    {'id': '235', 'language': 'en', 'text': 'Sophisticated'},
    {'id': '236', 'language': 'en', 'text': 'Spacey'},
    {'id': '237', 'language': 'en', 'text': 'Sparkling'},
    {'id': '238', 'language': 'en', 'text': 'Sparse'},
    {'id': '239', 'language': 'en', 'text': 'Spicy'},
    {'id': '240', 'language': 'en', 'text': 'Spiritual'},
    {'id': '241', 'language': 'en', 'text': 'Spontaneous'},
    {'id': '242', 'language': 'en', 'text': 'Spooky'},
    {'id': '243', 'language': 'en', 'text': 'Sprawling'},
    {'id': '244', 'language': 'en', 'text': 'Sprightly'},
    {'id': '245', 'language': 'en', 'text': 'Springlike'},
    {'id': '246', 'language': 'en', 'text': 'Stately'},
    {'id': '247', 'language': 'en', 'text': 'Street-Smart'},
    {'id': '248', 'language': 'en', 'text': 'Striding'},
    {'id': '249', 'language': 'en', 'text': 'Strong'},
    {'id': '250', 'language': 'en', 'text': 'Stylish'},
    {'id': '251', 'language': 'en', 'text': 'Suffocating'},
    {'id': '252', 'language': 'en', 'text': 'Sugary'},
    {'id': '253', 'language': 'en', 'text': 'Summery'},
    {'id': '254', 'language': 'en', 'text': 'Suspenseful'},
    {'id': '255', 'language': 'en', 'text': 'Swaggering'},
    {'id': '256', 'language': 'en', 'text': 'Sweet'},
    {'id': '257', 'language': 'en', 'text': 'Swinging'},
    {'id': '258', 'language': 'en', 'text': 'Technical'},
    {'id': '259', 'language': 'en', 'text': 'Tender'},
    {'id': '260', 'language': 'en', 'text': 'Tense/Anxious'},
    {'id': '261', 'language': 'en', 'text': 'Theatrical'},
    {'id': '262', 'language': 'en', 'text': 'Thoughtful'},
    {'id': '263', 'language': 'en', 'text': 'Threatening'},
    {'id': '264', 'language': 'en', 'text': 'Thrilling'},
    {'id': '265', 'language': 'en', 'text': 'Tough'},
    {'id': '266', 'language': 'en', 'text': 'Tragic'},
    {'id': '267', 'language': 'en', 'text': 'Transparent/Translucent'},
    {'id': '268', 'language': 'en', 'text': 'Trashy'},
    {'id': '269', 'language': 'en', 'text': 'Trippy'},
    {'id': '270', 'language': 'en', 'text': 'Triumphant'},
    {'id': '271', 'language': 'en', 'text': 'Tuneful'},
    {'id': '272', 'language': 'en', 'text': 'Turbulent'},
    {'id': '273', 'language': 'en', 'text': 'Uncompromising'},
    {'id': '274', 'language': 'en', 'text': 'Understated'},
    {'id': '275', 'language': 'en', 'text': 'Unsettling'},
    {'id': '276', 'language': 'en', 'text': 'Uplifting'},
    {'id': '277', 'language': 'en', 'text': 'Urgent'},
    {'id': '278', 'language': 'en', 'text': 'Virile'},
    {'id': '279', 'language': 'en', 'text': 'Visceral'},
    {'id': '280', 'language': 'en', 'text': 'Volatile'},
    {'id': '281', 'language': 'en', 'text': 'Vulgar'},
    {'id': '282', 'language': 'en', 'text': 'Warm'},
    {'id': '283', 'language': 'en', 'text': 'Weary'},
    {'id': '284', 'language': 'en', 'text': 'Whimsical'},
    {'id': '285', 'language': 'en', 'text': 'Wintry'},
    {'id': '286', 'language': 'en', 'text': 'Wistful'},
    {'id': '287', 'language': 'en', 'text': 'Witty'},
    {'id': '288', 'language': 'en', 'text': 'Wry'},
    {'id': '289', 'language': 'en', 'text': 'Yearning'}
]}

headers   = {"Ocp-Apim-Subscription-Key": sub_key}
sentiments = requests.post(sent_api, headers=headers, json=moods)
sent = sentiments.json()['documents']
pprint(sent)
#key_phrases = requests.post(key_api, headers=headers, json=documents)
#keys = key.json()

for i in sent:
    print(str(i['score']))
