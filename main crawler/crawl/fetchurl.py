import requests
from bs4 import BeautifulSoup
import os
urltuoitre = "https://tuoitre.vn/suc-khoe/dinh-duong/trang-1.htm"
bottomurls = []
pageurls = []
urls = []
basetuoitre = "https://tuoitre.vn"

urldantri = "https://dantri.com.vn/suc-khoe/tu-van/trang-2.htm"
basedantri = "https://dantri.com.vn"

urlvnexpress = "https://vnexpress.net/suc-khoe/dinh-duong-p2"


def fetchvnexpress(url, i, pageurls):
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
        url = url[:43] + str(i)
        return fetchvnexpress(url, i, pageurls)


def fetchdantri(url, i, pageurls, baseurl):
    print("Getting urls from page #" + str(i))
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    pagetags = soup.find_all(
        'div', class_='news-item news-item--timeline news-item--left2right')
    for pageurl in pagetags:
        pageurl = baseurl + pageurl.a.attrs["href"]
        pageurls.append(pageurl)
    if i == 30:
        return pageurls
    else:
        i += 1
        url = url[:44] + str(i) + ".htm"
        return fetchdantri(url, i, pageurls, baseurl)


def fetchtuoitre(url, i, bottomurls, pageurls, baseurl):
    print("Getting urls from page #" + str(i))
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

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
    if i == 30:
        return pageurls
    else:
        i += 1
        url = url[:45] + str(i) + ".htm"
        return fetchtuoitre(url, i, bottomurls, pageurls, baseurl)


def returndata():
    urls = []
    tuoitreurl = fetchtuoitre(urltuoitre, 1, bottomurls, pageurls, basetuoitre)
    dantriurl = fetchdantri(urldantri, 1, pageurls, basedantri)
    vnexpressurl = fetchvnexpress(urlvnexpress, 1, pageurls)
    urls.append(tuoitreurl)
    urls.append(dantriurl)
    urls.append(vnexpressurl)
    return urls
