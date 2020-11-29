import requests
from bs4 import BeautifulSoup
import os
url1 = "https://vnexpress.net/suc-khoe/dinh-duong-p2"
bottomurls = []
pageurls = []
urls = []
# baseurl = "https://dantri.com.vn"


def fetchpage(url, i, pageurls):
    print("Getting urls from page #" + str(i))
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    # focus-top
    topurl = soup.find(
        'article', class_='item-news full-thumb article-topstory')
    topurl = topurl.h2.a.attrs["href"]

    pagetags = soup.find_all(
        'article', class_='item-news item-news-common')
    for pageurl in pagetags:
        try:
            pageurl = pageurl.p.a.attrs["href"]
            pageurls.append(pageurl)
        except:
            continue

    if i == 2:
        return pageurls
    else:
        i += 1
        url = url1[:43] + str(i)
        return fetchpage(url, i, pageurls)


def returndata():
    urls = fetchpage(url1, 1, pageurls)
    return urls


returndata()
