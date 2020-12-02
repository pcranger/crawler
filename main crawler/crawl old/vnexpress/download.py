import requests
import re
from bs4 import BeautifulSoup
from PIL import Image
import os
import unidecode
import fetchurl


def download(url):
    # find the title
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    # find image tag
    vcs = soup.find_all('figure')
    # reformat h1 (header)
    h1 = soup.find('h1').text
    h1 = unidecode.unidecode(h1)
    h1 = re.sub(r'\W+', '', h1)
    # make a folder with h1
    if os.path.isdir(f'./download/{h1}') == False:
        os.mkdir(f'./download/{h1}')
    else:
        return
    images = []
    for i, vc in enumerate(vcs):
        # find and save image
        try:
            image_url = vc.img['data-src']
        except:
            break
        try:
            img = Image.open(requests.get(image_url, stream=True).raw)
        except:
            continue
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(f'./download/{h1}/image{i}.jpg')

        # find caption and save to .txt
        try:
            cap = vc.figcaption.p.text
            # fix caption
            if cap == "":
                cap = h1
            with open(f'./download/{h1}/caption{i}.txt', 'a', encoding='utf-8') as f:
                f.write(cap)
        except:
            continue


def exec():
    # get url from fetchurl.py and put it in an array
    urls = fetchurl.returndata()
    print("________________________________________________________")
    print("Downloading " + "articles: " + str(len(urls)))
    print("________________________________________________________")
    # create folder
    os.mkdir('download')

    for i, page in enumerate(urls):
        print("Fetching" + "(" + str(i) + "/" + str(len(urls)) + "): " + page)
        # start download picture function
        download(page)


# start function
exec()
