# Write code to access a favorite webpage and extract some text from it. For example, access a weather site and extract the forecast top
# temperature for your town or city today.

from urllib import request
from bs4 import BeautifulSoup
from nltk import word_tokenize
import nltk

# scrapes the webpage and cleans out the html
url = "http://www.accuweather.com/en/us/charlottesville-va/22902/weather-forecast/331243"
html = request.urlopen(url).read().decode('utf8')
soup = BeautifulSoup(html)
today = soup.find(class_="info city-fcast-text")
print(today.get_text())

# raw = BeautifulSoup(html).get_text()

# # tokenizes the text
# tokens = word_tokenize(raw)

# print(html)
# # pulls out today's forecast
# tokens = tokens[7986:8038]
# text = nltk.Text(tokens)

