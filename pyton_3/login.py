import requests 


usuario = 'cabralzay@yahoo.com' # http://192.168.0.104/phpmyadmin/index.php = pma_username && pma_password
url = 'http://httpbin.org/cookies'
#url = 'https://m.facebook.com'
#url2 = 'https://m.facebook.com/home.php'
# pyload = {'email': usuario, 'pass': 'Zzay90_,AO'}
pyload = {'pma_username': 'ifp', 'pma_password': 'ifp'}

r = requests.put('http://192.168.0.104/phpmyadmin/', params=pyload, allow_redirects=False)
r.url
r.status_code
#print(r.status_code)

if r.status_code == 301: # if respuesta.history[0].status_code in [301,302]:
    #print("Hay combinaciones")
    print(r.status_code)
    #break
else:
    print("HHH")


#my_file = open('passes.txt', 'r')
#for index in my_file.readlines():

#print(my_file.read())
    #print(index)

#my_file.close()
