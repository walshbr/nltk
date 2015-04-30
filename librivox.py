from contextlib import closing
from urllib import request
from bs4 import BeautifulSoup
import re
import math
import time
import random
import sqlite3
import os


posts = []
counter = 0
max_sleep = 2.0
post_counter = 1

FORUM = 'f'
TOPIC = 't'


def download(url):
    time.sleep(random.random() * max_sleep)
    print('DOWNLOAD {}'.format(url))
    html = request.urlopen(url).read().decode('utf8', errors='replace')
    return BeautifulSoup(html)


def get_urls(soup, class_, key, parent_id):
    """ Returns a tuple (key, URL, ID, text). """
    begin_pattern = re.compile(r'^\.')
    end_pattern = re.compile(r'&sid=.+$')
    urls = []
    for a in soup.find_all(class_=class_):
        url = a.get('href')
        if not url:
            continue
        url = end_pattern.sub('', url)
        url = begin_pattern.sub('https://forum.librivox.org', url)
        urls.append((key, url, parent_id, a.get_text()))
    return urls


def get_work(cxn):
    """\
    Retrieve one unscraped URL from the database and update its scraped field.

    Each work item is a three-part tuple listing the item's ID, URL, and level.
    """
    with closing(cxn.cursor()) as c:
        c.execute('''
            SELECT id, url, level
                FROM urls
                WHERE scraped IS NULL
                LIMIT 1;
            ''')
        work = c.fetchone()
        if work is not None:
            c.execute("UPDATE urls SET scraped=datetime('now') WHERE id=?;",
                      (work[0],))
        return work


def enqueue_urls(cxn, urls):
    """This takes the output of get_urls and inserts them into the db."""
    with closing(cxn.cursor()) as c:
        print('enqueue_urls: {}'.format(urls))
        c.executemany(
            '''INSERT OR IGNORE INTO urls
                (level, url, parent_url_id, text)
                VALUES (?, ?, ?, ?);''',
            urls,
            )
        print('ENQUEUED {}'.format(c.rowcount))


def get_enqueue_urls(cxn, soup, class_, key, parent_id):
    """Get the urls via 'get_urls' and puts them into the database."""
    enqueue_urls(cxn, get_urls(soup, class_, FORUM, parent_id))


def scrape_posts(url):
    """\
    Scrapes Librivox posts and appends the content of each post to a list
    containing its posts.
    """
    page_posts = []
    # gets the url
    soup = download(url)

    # gets the text of the posts and appends them to the posts list.
    soup_posts = soup.find_all(class_="postbody")
    for post in soup_posts:
        post_text = post.get_text()
        # only pulls in those posts not prefaced with underscores (because
        # those are going to be user signatures)
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
    """\
    For a given forum or topic it pulls out the number of pages that need to be
    spidered.
    """
    # should really be refactored so that it's a single function that
    # identifies whether or not you're on an individual forums page or not.
    #
    # pulls in the soup. should probably refactor this so it's not done twice.
    soup = download(url)

    # pulls in the things that have the class they are using for the tag.
    tags = soup.find_all(class_='gensmall')
    tags = [tag.get_text() for tag in tags]

    # does a regex over their tags to find the number of pages using the format
    # they usually use.
    for tag in tags:

        if re.findall(r'\[\s([0-9]+)\stopic', tag):
            number_of_topics = re.findall(r'\[\s([0-9]+)', tag)
            number_of_pages = math.ceil(int(number_of_topics[0]) / 50)

        elif re.findall(r'\[\s([0-9]+\spost)', tag):
            number_of_posts = re.findall(r'\[\s([0-9]+)', tag)
            number_of_pages = math.ceil(int(number_of_posts[0]) / 15)

    return number_of_pages


def insert_posts(cxn, posts):
    """Take the output of scrape_topic and insert it into the posts."""
    with closing(cxn.cursor()) as c:
        c.executemany('INSERT INTO postings (url_id, text) AS (?, ?);', posts)


def scrape_topic(topic_url, topic_id):
    """scrapes all posts from a topic"""
    output = []
    counter = 0
    global post_counter

    # a counter to show the progress through the given topic
    num_pages = find_number_of_pages_or_topics(topic_url)

    # assigns the forum urls start
    url = topic_url + '&start=0'

    # scrapes the posts for each page in the forum.
    while counter < num_pages:
        url = paginator(url, counter, 15)
        posts = scrape_posts(url)
        for post in posts:
            output.append((str(topic_id), str(post).replace('\t', ' ')))
            print(url + '    ' + str(post_counter))
            post_counter += 1
        counter += 1

    return output


def get_all_topic_links_in_a_forum(forum_url, forum_id):
    """gets all the topic links in a forum."""
    links = []
    counter = 0
    num_pages = find_number_of_pages_or_topics(forum_url)

    url = forum_url + '&start=0'

    while counter < num_pages:
        url = paginator(url, counter, 50)
        page_links = get_topic_links_for_a_page(url, forum_id)
        links.extend(page_links)
        counter += 1

    return(links)


def get_topic_links_for_a_page(forum_url, forum_id):
    """Gets all of the links for the topics contained in a forum."""
    # note: it only does this for one page. You need to paginate
    # pulls in all the raw links with the topic title class.
    return get_urls(download(forum_url), 'topictitle', TOPIC, forum_id)


def scrape_forum(forum_url, forum_id):
    """Scrapes all the topics for a given forum."""

    # for every topic in a forum, scrape all the posts and put it in a
    # single list.
    return get_all_topic_links_in_a_forum(forum_url, forum_id)


def scrape_everything():
    """scrapes everything. punch it chewie."""
    # pulls in the main index page
    with open_db('librivox.db') as cxn:
        soup = download('https://forum.librivox.org/index.php')
        get_enqueue_urls(cxn, soup, 'forumlink', FORUM, None)
        cxn.commit()

        while True:
            try:
                work = get_work(cxn)
                if work is None:
                    break
                print('WORK: {}'.format(work))

                if work[2] == FORUM:
                    enqueue_urls(cxn, scrape_forum(work[1], work[0]))
                elif work[2] == TOPIC:
                    insert_posts(cxn, scrape_topic(work[1], work[0]))

            except:
                cxn.rollback()
                raise

            else:
                cxn.commit()


def open_db(filename):
    exists = os.path.exists(filename)
    cxn = sqlite3.connect(filename)

    if not exists:
        with closing(cxn.cursor()) as c:
            c.executescript('''
                CREATE TABLE urls (
                    id INTEGER PRIMARY KEY,
                    url TEXT UNIQUE NOT NULL,
                    parent_url_id INTEGER,
                    level TEXT,
                    text TEXT,
                    added REAL DEFAULT (datetime('now')),
                    scraped REAL DEFAULT NULL
                    );
                CREATE TABLE postings (
                    id INTEGER PRIMARY KEY,
                    url_id INTEGER,
                    text TEXT,
                    scraped REAL DEFAULT (datetime('now'))
                    );
                ''')
            cxn.commit()

    return cxn


if __name__ == '__main__':
    scrape_everything()

# scrape_forum('https://forum.librivox.org/viewforum.php?f=18')
