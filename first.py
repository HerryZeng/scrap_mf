from urllib.request import urlopen
import re

url = "https://morvanzhou.github.io/static/scraping/basic-structure.html"
html = urlopen(url).read().decode('utf-8')
# print(html)

ress = re.findall(r'<title>(.+?)</title>',html)
print(type(ress))
for res in ress:
    print("\nPage title is :",res)

ress = re.findall(r'<p>(.*?)</p>',html,flags=re.DOTALL)
print(len(ress))
for res in ress:
    print("\nPage P is :",res)

ress = re.findall(r'href="(.*?)"', html, flags=re.DOTALL)
print(len(ress))
for res in ress:
    print("\nPage P is :", res)