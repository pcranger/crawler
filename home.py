import requests
from bs4 import BeautifulSoup
import os
url1 = "https://tuoitre.vn/suc-khoe/dinh-duong/trang-1.htm"


def fetchpage(url, i):
    req = requests.get(url)
    print(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    # focus-top
    baseurl = "https://tuoitre.vn"

    topurl = soup.find('a', class_='focus-top-title').attrs["href"]

    # focus-bottom
    bottomurls = []
    bottomtags = soup.find_all('a', class_='focus-middle-title')
    for bottomurl in bottomtags:
        bottomurl = baseurl + bottomurl.attrs["href"]
        bottomurls.append(bottomurl)
    # news-item

    pageurls = []
    pagetags = soup.find_all('h3', class_='title-news')
    for pageurl in pagetags:
        pageurl = baseurl + pageurl.a.attrs["href"]
        print("fetching " + pageurl)
        pageurls.append(pageurl)

    url = url[:45] + str(i) + ".htm"
    print(url)
    fetchpage(url, i+1)


fetchpage(url1, 2)
