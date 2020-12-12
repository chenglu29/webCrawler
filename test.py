#no recursion

from collections import deque
import urllib.request
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
from urllib.error import HTTPError
import re

queue=deque([])


url=("http://engineering.nyu.edu/")
def crawl(url):
    try:
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page)
        links=[]
        print("*************every time the url is crawled**********")
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            print (link.get('href'))
    except HTTPError as e:
        print(e)
        if e.code==403:
            print("error 403")

crawl(url)

    
