from pprint import pprint
d = { 'red': 3, 'blue': 3}

pprint([key for key, value in d.items() if value == 3])
