# ◑ Write code to convert nationality adjectives like Canadian and Australian to their corresponding nouns Canada and Australia (see http://en.wikipedia.org/wiki/List_of_adjectival_forms_of_place_names).

import re
import nltk
import pycountry

countries = [country.name for country in pycountry.countries]

def convert(word):
	tup = re.findall(r'^(.*)(ese|ian|an|ean|n|ic|ern)', word)
	country = tup[0][0]
	if country in countries:
		return country
	else:
		print("Problem with stemmer or country list. Result is: " + str(country))

print(convert('American'))
