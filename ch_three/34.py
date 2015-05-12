# ◑ Write code to convert nationality adjectives like Canadian and Australian to their corresponding nouns Canada and Australia (see http://en.wikipedia.org/wiki/List_of_adjectival_forms_of_place_names).

import re
import nltk
import pycountry

countries = [country.name for country in pycountry.countries]




def convert(word):
	"""converts an adjectival nationality to its corresponding noun form."""

	# list of regex things to check
	patterns = ['ese', 'ian', 'an', 'ean', 'n', 'ic', 'ern']
	#list of suffixes for appending to country names that get damaged when they are split.
	suffixes = ['a', 'o']

	# for every potential way of forming a nationality adjective, test them.
	for pattern in patterns:
		tup = re.findall(r'^(.*)(' + pattern + ')', word)

		#if the regex finds a pattern, set the country to the stem of the word.

		if tup:
			country = tup[0][0]

			# check to see if the country is in the list of countries returned by pycountry. If it is, return it.
			if country in countries:
				return country

			# if the stem is not a country, try adding suffixes to it to see if you can pull out a real country.

			else:
				for suffix in suffixes:
					new_country = country + suffix
					if new_country in countries:
						return new_country

print(convert('Mexican'))
