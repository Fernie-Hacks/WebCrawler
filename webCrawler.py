#Module to request information from a webpage
import request

#Beautiful soup allows for neat and easy access to links
from bs4 import BeautifulSoup

keyWord = input("Enter a Key Word: ")

def web_spider(max_pages, keyWord):
    page = 1;
    while page <= max_pages:
        StartingURL = 'https://www.google.com/#safe=off&q=' + keyWord
        websiteCode = request.get(url)
        websitePlainText = websiteCode.text
        websiteSoupObject = BeautifulSoup(websitePlainText)
        for link in websiteSoupObject.findAll('a', {'class': 'r'}):
            href = link.get('href')
        page += 1

web_spider(1, keyWord)
