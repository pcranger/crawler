import requests
from bs4 import BeautifulSoup
import os
url1 = "https://tuoitre.vn/suc-khoe/dinh-duong/trang-1.htm"
bottomurls = []
pageurls = []
urls = []


def fetchpage(url, i, bottomurls, pageurls):
    print("Getting urls from page #" + str(i))
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    baseurl = "https://tuoitre.vn"

    # focus-top
    topurl = soup.find('a', class_='focus-top-title').attrs["href"]

    # focus-bottom
    bottomtags = soup.find_all('a', class_='focus-middle-title')
    for bottomurl in bottomtags:
        bottomurl = baseurl + bottomurl.attrs["href"]
        bottomurls.append(bottomurl)

    # news-item
    pagetags = soup.find_all('h3', class_='title-news')
    for pageurl in pagetags:
        pageurl = baseurl + pageurl.a.attrs["href"]
        pageurls.append(pageurl)
    if pagetags == []:
        return pageurls
    else:
        i += 1
        url = url[:45] + str(i) + ".htm"
        return fetchpage(url, i, bottomurls, pageurls)


def returndata():
    urls = fetchpage(url1, 1, bottomurls, pageurls)
    return urls
