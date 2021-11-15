import requests 
r = requests.get('http://github.com')
url = 'http://httpbin.org/cookies'
r.url
r.status_code
#print (r.history[0].status_code)


if r.history[0].status_code == 301: # if respuesta.history[0].status_code in [301,302]:
    print("Hay combinaciones")
    # print(r.status_code)
    #break
else:
    print("NADA")