import requests 
s = requests.Session()
s.verify = 'path/to/CAs'
r = requests.get('https://github.com', verify=False)

print(r.text)