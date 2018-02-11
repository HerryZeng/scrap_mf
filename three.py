import random
import re
import ssl
from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from logging import config

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB"]
h1_list = ['网络爬虫']
print(parse.quote(h1_list[-1]))
for i in range(20):
    # url = base_url + parse.quote(his[-1])
    url = base_url + his[-1]
    # print(url)

    html = urlopen(url)
    soup = BeautifulSoup(html, features='lxml')
    print(soup.find("h1").get_text(), "URL:", his[-1])

    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
    # for sub_url in sub_urls:
    #     print(sub_url)
    if len(sub_urls) != 0:
        sub_url = random.sample(sub_urls, 1)[0]['href']
        his.append(sub_url)
        h1_list.append(parse.unquote(sub_url[6:]))
    else:
        his.pop()
# print(his)
# print(h1_list)
config.fileConfig('log_settings')

