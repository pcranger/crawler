import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
import lmao


def download(url):
    # find the title
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    # find image tag
    vcs = soup.find_all('div', class_='VCSortableInPreviewMode')
    # find date and time tag
    datetime = soup.find('div', class_='date-time').text
    # reformat datetime
    datetime = ' '.join(datetime.split()[0:2])
    datetime = datetime.replace("/", "-")
    datetime = datetime.replace(":", "")
    # make a folder with datetime
    if os.path.isdir(f'./{datetime}') == False:
        os.mkdir(f'./{datetime}')
    images = []
    n = len(vcs) - 1
    vcs = vcs[:n]
    for i, vc in enumerate(vcs):
        # find caption and save to .txt
        cap = vc.find('p').text
        with open(f'./{datetime}/caption{i}.html', 'a', encoding='utf-8') as f:
            f.write(cap)
        # find and save image
        try:
            image_url = vc.div.img['src']
        except:
            break
        img = Image.open(requests.get(image_url, stream=True).raw)
        img.save(f'./{datetime}/image{i}.jpg')


def exec():
    urls = lmao.returndata()
    print("________________________________________________________")
    print("Downloading")
    print("________________________________________________________")
    for i in urls:
        print("downloading " + i)
        download(i)
    pass


exec()
