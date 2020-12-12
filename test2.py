from collections import deque
import urllib.request
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
from urllib.error import HTTPError
import re

queue=deque([])
visitedList=[]

url=("https://www.bing.com/search?q=polytech")
def crawl(url):
    try:
        visitedList.append(url)
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page)
        links=[]
        print("*************every time the url is crawled**********")
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            flag=0
            print (link.get('href'))
            for n in visitedList:
                if n==link.get("href"):
                    flag=1
                    break
                if flag==0:
                    queue.append(link.get("href"))
            current=queue.popleft()
            crawl(current)
    except HTTPError as e:
        print(e)
        if e.code==403:
            print("error 403")

crawl(url)
print("********visited pages********")
for m in visitedList:
    print(m)
    
