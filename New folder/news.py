#display news content
import requests
from bs4 import BeautifulSoup
import json


def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        print(headline.text)


url = 'https://www.cnbc.com/world/?region=world'
response = requests.get(url)
print_headlines(response.text)