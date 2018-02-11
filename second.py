from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging

url="https://morvanzhou.github.io/static/scraping/basic-structure.html"
html=urlopen(url).read().decode("utf-8")
# print(html)
soup = BeautifulSoup(html,features='lxml')
print(soup.h1)
all_href=soup.find_all('a')
all_href = [link['href'] for link in all_href]
print(all_href)

logging.basicConfig(level=logging.INFO,
         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
         datefmt='[%Y-%m-%d %H:%M:%S]',
         filename='info.log',
         filemode='a')

logging.info(all_href)
# for a in all_href:
#     # print(a.text)
#     print(a.attrs['href'])