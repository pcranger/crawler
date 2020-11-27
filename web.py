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
    if os.path.isdir(f'./download/{datetime}') == False:
        os.mkdir(f'./download/{datetime}')
    images = []
    n = len(vcs) - 1
    vcs = vcs[:n]
    for i, vc in enumerate(vcs):
        # find and save image
        try:
            image_url = vc.div.img['src']
        except:
            break
        img = Image.open(requests.get(image_url, stream=True).raw)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(f'./download/{datetime}/image{i}.jpg')

        # find caption and save to .txt
        try:
            cap = vc.find('p').text
            with open(f'./download/{datetime}/caption{i}.html', 'a', encoding='utf-8') as f:
                f.write(cap)
        except:
            continue
            # fix caption


def exec():
    # urls = lmao.returndata()
    # print("________________________________________________________")
    # print("Downloading")
    # print("________________________________________________________")
    # if os.path.isdir('downloads') == False:
    #     os.mkdir('download')
    # for i in urls:
    #     print("downloading " + i)
    #     download(i)
    # pass
    download('https://tuoitre.vn/dia-thuc-an-bo-duong-cua-chuyen-gia-dinh-duong-harvard-20181210143108105.htm')


exec()
