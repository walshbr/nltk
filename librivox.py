from urllib import request
from urllib import parse as urlparse
from bs4 import BeautifulSoup
import re
from nltk import word_tokenize
from nltk.corpus import words
import math
import time
import random

posts =[]
counter = 0
max_sleep = 2.0
post_counter = 1

def download(url):
    time.sleep(random.random() * max_sleep)
    html = request.urlopen(url).read().decode('utf8')
    return BeautifulSoup(html)


def get_urls(soup, class_, key):
    """ Returns a tuple (URL, ID, text). """
    begin_pattern = re.compile(r'^\.')
    end_pattern = re.compile(r'&sid=.+$')
    urls = []
    for a in soup.find_all(class_=class_):
        url = a.get('href')
        if not url:
            continue
        url = end_pattern.sub('', url)
        url = begin_pattern.sub('https://forum.librivox.org', url)
        # Parse the URL to get the page's identifier.
        urlp = urlparse.urlparse(url)
        qs = urlparse.parse_qs(urlp.query)
        ids = [int(url_id) for url_id in qs.get(key, ['-1'])]

        urls.append((url, ids[0], a.get_text()))
    return urls


def scrape_posts(url):
        """Scrapes Librivox posts and appends the content of each post to a list containing its posts"""
        page_posts = []
        #gets the url
        soup = download(url)

        #gets the text of the posts and appends them to the posts list.
        soup_posts = soup.find_all(class_="postbody")
        for post in soup_posts:
                post_text = post.get_text()
                # only pulls in those posts not prefaced with underscores (because those are going to be user signatures)
                if not re.findall(r'_+', post_text):
                        page_posts.append(post_text)

        return page_posts


def paginator(url, counter, per_page):

        # need a regex to find the last number of the url, the pagination number.
        pattern = re.compile(r'[0-9]+$')

        # initializes the counter.
        new_count = str(counter * per_page)
        if new_count == 0:
                return url
        # substitutes in the counter at the point in the strig.
        new_url = pattern.sub(new_count, url)
        return new_url

def has_link_and_class(tag):
        return tag.has_attr('a') and tag.has_attr(class_='row1')

def find_number_of_pages_or_topics(url):
        """For a given forum or topic it pulls out the number of pages that need to be spidered."""
        #should really be refactored so that it's a single function that identifies whether or not you're on an individual forums page or not.
        # pulls in the soup. should probably refactor this so it's not done twice.
        soup = download(url)

        # pulls in the things that have the class they are using for the tag.
        tags = soup.find_all(class_='gensmall')
        tags = [tag.get_text() for tag in tags]

        # does a regex over their tags to find the number of pages using the format they usually use.
        for tag in tags:

                if re.findall(r'\[\s([0-9]+)\stopic', tag):
                        number_of_topics = re.findall(r'\[\s([0-9]+)', tag)
                        number_of_pages = math.ceil(int(number_of_topics[0]) / 50)

                elif re.findall(r'\[\s([0-9]+\spost)', tag):
                        number_of_posts = re.findall(r'\[\s([0-9]+)', tag)
                        number_of_pages = math.ceil(int(number_of_posts[0]) / 15)

        return number_of_pages

def scrape_topic(forum_id, forum_name, topic_url, topic_id, topic_name):
        """scrapes all posts from a topic"""
        output = open('output.txt', 'a')
        counter = 0
        global post_counter

        # a counter to show the progress through the given topic


        num_pages = find_number_of_pages_or_topics(topic_url)

        # assigns the forum urls start
        url = topic_url + '&start=0'

        #scrapes the posts for each page in the forum.
        while counter < num_pages:
                url = paginator(url, counter, 15)
                posts = scrape_posts(url)
                for post in posts:
                        output.write('\t'.join([
                            str(forum_id), forum_name,
                            str(topic_id), topic_name,
                            str(post.replace('\t', ' ')),
                            ]))
                        output.write('\n\n\n')
                        print(url + '    ' + str(post_counter))
                        post_counter += 1
                counter += 1

        output.close

def get_all_topic_links_in_a_forum(forum_url):
        """gets all the topic links in a forum."""
        links = []
        counter = 0
        num_pages = find_number_of_pages_or_topics(forum_url)

        url = forum_url + '&t='

        while counter < num_pages:
                url = paginator(url, counter, 50)
                page_links = get_topic_links_for_a_page(forum_url)
                links.extend(page_links)
                counter += 1

        return(links)


def get_topic_links_for_a_page(forum_url):
        """Gets all of the links for the topics contained in a forum."""
        # note: it only does this for one page. You need to paginate
        # pulls in all the raw links with the topic title class.
        return get_urls(download(forum_url), 'topictitle', 't')

def scrape_forum(forum_url, forum_id, forum_name):
        """Scrapes all the topics for a given forum."""

        # for every topic in a forum, scrape all the posts and put it in a single list.
        for link_info in get_all_topic_links_in_a_forum(forum_url):
                scrape_topic(forum_id, forum_name, *link_info)

def scrape_everything():
        """scrapes everything. punch it chewie."""
        # pulls in the main index page
        soup = download('https://forum.librivox.org/index.php')
        for forum_info in get_urls(soup, 'forumlink', 'f'):
                scrape_forum(*forum_info)

if __name__ == '__main__':
    scrape_everything()

# scrape_forum('https://forum.librivox.org/viewforum.php?f=18')


