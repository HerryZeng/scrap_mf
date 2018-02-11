import requests

file = {'uploadFile': open('image.png', 'rb')}
url = "http://pythonscraping.com/files/processing2.php"

r = requests.post(url, files=file)
print(r.text)

# file = {'uploadFile': open('./image.png', 'rb')}
# r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
# print(r.text)