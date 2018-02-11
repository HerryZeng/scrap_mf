import os

import requests
from bs4 import BeautifulSoup

url = 'http://www.nationalgeographic.com.cn/animals/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
img_url = soup.find_all("ul", {"class": "img_list"})
print(type(img_url))

os.makedirs("image", exist_ok=True)

for ul in img_url:
    images = ul.find_all("img")
    for image in images:
        url = image['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open("image/%s" % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)

        print("Saved %s" % image_name)
