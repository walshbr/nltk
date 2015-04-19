# Write code to access a favorite webpage and extract some text from it. For example, access a weather site and extract the forecast top
# temperature for your town or city today.

from urllib import request
from bs4 import BeautifulSoup

url = "http://www.weather.com"
response = request.urlopen(url)
raw = response.read().decode('utf8')

text = BeautifulSoup(raw).get_text()