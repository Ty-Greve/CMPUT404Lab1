import requests 

print(requests.__version__)

url = "http://google.com"
res = requests.get(url)
print(res)
