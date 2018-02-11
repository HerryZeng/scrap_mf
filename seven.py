from urllib.request import urlretrieve,urlopen
import requests

url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
#使用urlretrieve下载
# urlretrieve(url, './image/learning_step_flowchart.png')
#使用requests下载
# r = requests.get(url)
# with open("image/abc.png",'wb') as f:
#     f.write(r.content)
#使用request的高效方法,下载大文件
r = requests.get(url,stream=True)
with open("image/efd.png",'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
