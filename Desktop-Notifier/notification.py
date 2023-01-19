# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:53:05 2022

@author: VAGUE
"""

from plyer import notification
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

def drink_water():
    title = "Time to Get Hydrated !!"
    message = "Get up and drink a glass of water"
    while True:
        notification.notify(
            title = title,
            message = message,
            timeout = 5
        )
        time.sleep(1800)

# source - https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en
def news_headlines():
    url = "https://news.google.com/news/rss"
    xml_data = urlopen(url).read()
    urlopen(url).close()
    
    sp = BeautifulSoup(xml_data, 'xml')
    news_list = sp.find_all('item')
    news_list = news_list[0:5]
    
    for news in news_list:    
        message = news.title.text + '\n Published on: ' + news.pubDate.text
        print(message)
        print("")
        
    for news in news_list:
        notification.notify(
            title = "Top Headlines of Today !!",
            message = news.title.text + '\nPublished on: ' + news.pubDate.text,
            timeout = 5
        )

if __name__ == "__main__":
    news_headlines()