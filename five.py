import requests

# url="http://pythonscraping.com/pages/files/form.html"
url = "http://pythonscraping.com/pages/files/processing.php"

data = {"firstname": "栋梁", "lastname": "曾"}
r = requests.post(url, data=data)
print(r)
print(r.text)
