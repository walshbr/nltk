from urllib import request
from bs4 import BeautifulSoup
import re
from nltk import word_tokenize
from nltk.corpus import words

url = "https://forum.librivox.org/viewtopic.php?f=16&t=26004&start=0"
posts =[]
counter = 0

def scrape(url):
	"""Scrapes a Librivox post and appends the content of its posts to a list containing its posts"""

	#gets the url
	html = request.urlopen(url).read().decode('utf8')
	soup = BeautifulSoup(html)
	
	#gets the text of the posts and appends them to the posts list.
	soup_posts = soup.find_all(class_="postbody")
	for post in soup_posts:
		post_text = post.get_text()
		# only pulls in those posts not prefaced with underscores (because those are going to be user signatures)
		if not re.findall(r'_+', post_text):
			posts.append(post_text)


def paginator(url, counter):

	# need a regex to find the last number of the url, the pagination number.
	pattern = re.compile(r'[0-9]+$')

	# initializes the counter.
	new_count = str(counter * 15)
	if new_count == 0:
		return url
	# substitutes in the counter at the point in the strig.
	new_url = pattern.sub(new_count, url)
	return new_url

# calls down a url using the paginator function and adds one to the counter each time, paginating through the forum and adding to the posts collection as it goes.

def find_page_numbers(url):
	"""Finds the number of pages in the post by pulling in the number of posts from the scraped thing."""

	# pulls in the soup. should probably refactor this so it's not done twice.
	html = request.urlopen(url).read().decode('utf8')
	soup = BeautifulSoup(html)

	# pulls in the things that have the class they are using for the tag.
	tags = soup.find_all(class_='gensmall')
	tags = [tag.get_text() for tag in tags]

	# does a regex over their tags to find the page number using the format they usually use. 
	for tag in tags:
		if re.findall(r'\[\s([0-9]+)', tag):
			number_of_posts = re.findall(r'\[\s([0-9]+)', tag)

	# returns the number of pages by dividing the number of posts by the number of pages.
	number_of_pages = int(number_of_posts[0]) / 15	
	number_of_pages = int(number_of_pages)
	return number_of_pages

#finds the number of pages
num_pages = find_page_numbers(url)

#scrapes the posts for each page in the forum.
while counter < num_pages:
	url = paginator(url, counter)
	scrape(url)
	counter += 1

# prints the number of posts	
print(posts)

