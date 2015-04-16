# ☼ Write a utility function that takes a URL as its argument, 
# and returns the contents of the URL, with all HTML markup removed. 
# Use from urllib import request and then request.urlopen('http://nltk.org/').read().decode('utf8') 
# to access the contents of the URL.

from urllib import request
from bs4 import BeautifulSoup

def utility(url):
	link = url
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html).get_text()
	print(raw)

utility('http://nltk.org')