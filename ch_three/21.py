# ◑ Write a function unknown() that takes a URL as its argument, and returns a list of unknown words that occur on that webpage. In order to do this, extract all substrings consisting of lowercase letters (using re.findall()) and remove any items from this set that occur in the Words Corpus (nltk.corpus.words). Try to categorize these words manually and discuss your findings.

from urllib import request
from bs4 import BeautifulSoup
import re
from nltk import word_tokenize
from nltk.corpus import words

def unknown(url):
	"""Takes a URL as its argument and returns a list of unknown words that occur on that webpage."""
	
	# gets the text of the page
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html).get_text()
	junk = set(words.words())
	# finds the lower case words by searching for a word boundary plus one or more lower case letters
	lower_case_words = re.findall(r'\b[a-z]+', raw)

	# searches through the list of lower case words and gets rid of those not in the words corpus.
	unknowns = [word for word in lower_case_words if word not in junk]
	print(unknowns)

unknown('http://www.nltk.org/book/ch03.html')

