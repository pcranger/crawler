import requests
import re
from bs4 import BeautifulSoup
from PIL import Image
import unidecode
import fetchurl
import json


def downloaddantri(url):
    article = {
        "header": "",
        "image": [],
        "caption": []
    }
    # find the title
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    # find image tag
    vcs = soup.find_all('figure')
    # find h1
    try:
        h1 = soup.find_all('h1')[1].text
    except:
        h1 = soup.find_all('h1')[0].text
    h1 = unidecode.unidecode(h1)
    h1 = re.sub(r'\W+', '', h1)
    article["header"] = h1
    images = []
    for i, vc in enumerate(vcs):
        # find and save image
        try:
            image_url = vc.img['src']
        except:
            break
        if "https" not in image_url:
            image_url = 'https:' + image_url
        article['image'].append(image_url)

        # find caption and save to .txt
        try:
            cap = vc.figcaption.p.text
            # fix caption
            if cap == "":
                cap = h1
        except:
            continue
        return article


def downloadvnexpress(url):
    article = {
        "header": "",
        "image": [],
        "caption": []
    }
    # find the title
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    # find image tag
    vcs = soup.find_all('figure')
    # reformat h1 (header)
    try:
        h1 = soup.find('h1').text
        h1 = unidecode.unidecode(h1)
        h1 = re.sub(r'\W+', '', h1)
        article["header"] = h1
    except:
        pass
    images = []
    for i, vc in enumerate(vcs):
        # find and save image
        try:
            image_url = vc.img['data-src']
        except:
            break
        article['image'].append(image_url)
        # find caption and save to .txt
        try:
            cap = vc.figcaption.p.text
            # fix caption
            if cap == "":
                cap = h1
        except:
            continue
        article['caption'].append(cap)
    return article


def downloadtuoitre(url):
    article = {
        "header": "",
        "image": [],
        "caption": []
    }
    # find the title
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    # find image tag
    vcs = soup.find_all('div', class_='VCSortableInPreviewMode')
    if vcs == []:
        vcs = soup.find_all('div', class_='content fck')
    h1 = soup.find('h1').text
    h1 = unidecode.unidecode(h1)
    h1 = re.sub(r'\W+', ' ', h1)
    article["header"] = h1
    images = []
    for i, vc in enumerate(vcs):
        # find image
        try:
            image_url = vc.img['src']
        except:
            break
        if "https" not in image_url:
            image_url = 'https:' + image_url
        article['image'].append(image_url)
        # find caption
        try:
            cap = vc.figcaption.p.text
            print(cap)
            # fix caption
            if cap == "":
                cap = h1
        except:
            continue
        article['caption'].append(cap)

    return article


def exec():
    data = {
        'tuoitre': [],
        'vnexpress': [],
        'dantri': []
    }
    # get url from fetchurl.py and put it in an array
    urls = fetchurl.returndata()
    print("________________________________________________________")
    print("Fetching " +
          str(len(urls[0]) + len(urls[1]) + len(urls[2])) + " articles ")
    print("________________________________________________________")
    for i, page in enumerate(urls[0]):
        print("Fetching" + "(" + str(i) + "/" +
              str(len(urls[0])) + "): " + page)
        tuoitredata = downloadtuoitre(page)
        data['tuoitre'].append(tuoitredata)
    print("donetuoitre")

    for i, page in enumerate(urls[1]):
        print("Fetching" + "(" + str(i) + "/" +
              str(len(urls[1])) + "): " + page)
        dantridata = downloaddantri(page)
        data['dantri'].append(dantridata)
    print("donedantri")

    for i, page in enumerate(urls[2]):
        print("Fetching" + "(" + str(i) + "/" +
              str(len(urls[2])) + "): " + page)

        vnexpressdata = downloadvnexpress(page)
        data['vnexpress'].append(vnexpressdata)
    print("donevnexpress")

    pass
    return data


data = exec()
with open('data.json', 'w') as f:
    json.dump(data, f)
