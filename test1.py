import requests 

print(requests.__version__)

url = "https://raw.githubusercontent.com/Ty-Greve/CMPUT404Lab1/main/test1.py"
res = requests.get(url)
print(res.text)
