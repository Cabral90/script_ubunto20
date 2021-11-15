import requests

r = requests.head('http://github.com', allow_redirects=True) # http://www.facebook.com # http://github.com
# r = requests.get('http://github.com', allow_redirects=False) # http://www.facebook.com # http://github.com
print(r.url)
print(r.status_code)
# code = r.history[0].status_code
print(r.history)