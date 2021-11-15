import requests

s = requests.Session()

username = { 'username': 'Jose55'}
location = {'location': 'Spanish'}

setCookieUrl = 'https://httpbin.org/cookies/set'
getCookiesUrl = 'https://httpbin.org/cookies'

s.get(setCookieUrl, params=username)
s.get(setCookieUrl, params=location)

r = s.get(getCookiesUrl)
s.__exit__
#print(r.text)