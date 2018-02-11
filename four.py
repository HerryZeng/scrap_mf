import requests
import webbrowser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

param = {"wd":"莫烦Python"}
r = requests.get('http://www.baidu.com/s',params=param)
print(r.url)
webbrowser.open(r.url)
