import requests

url = 'https://httpbin.org/redirect-to'
params = {"status-code": 301, "url": "https://stackoverflow.com/q/22150023"}
r = requests.get(url, params=params)
r.history 
#[<Response[301]>, <Response [302]>]
print(r.history[0].status_code)


#r = requests.get('http://goo.gl/Nzek5', allow_redirects=False)

#print (r.history)