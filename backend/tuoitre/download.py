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
    vcs = soup.find_all('div', class_='VCSortableInPreviewMode')
    if vcs == []:
        vcs = soup.find_all('div', class_='content fck')
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
            image_url = vc.img['src']
            print("    downloading image: " + image_url)
        except:
            break
        try:
            img = Image.open(requests.get(image_url, stream=True).raw)
        except:
            image_url = 'https:' + image_url
            img = Image.open(requests.get(image_url, stream=True).raw)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(f'./download/{h1}/image{i}.jpg')

        # find caption and save to .txt
        try:
            cap = vc.find('p').text
            with open(f'./download/{h1}/caption{i}.txt', 'a', encoding='utf-8') as f:
                f.write(cap)
        except:
            continue
            # fix caption


def exec():
    urls = fetchurl.returndata()
    print("________________________________________________________")
    print("Downloading")
    print("________________________________________________________")
    os.mkdir('download')
    for i in urls:
        print("Fetching " + i)
        download(i)
    pass


exec()
