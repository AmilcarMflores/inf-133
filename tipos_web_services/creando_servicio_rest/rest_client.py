# Importando la librería requests, que se utiliza para hacer solicitudes HTTP
import requests
# Definición de la URL base del servidor local
url = "http://localhost:8000/"

# Realizando una solicitud GET a la ruta /lista_estudiantes del servidor local
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
# Imprimiendo la respuesta obtenida
print(get_response.text)

# Creando un nuevo estudiante para agregar al servidor
nuevo_estudiante = {
  "nombre": "Juanito",
  "apellido": "Pérez",
  "carrera": "Ingenieria Agronómica",
}

# Realizando una solicitud POST para agregar un nuevo estudiante a la ruta /agrega_estudiante del servidor local
ruta_post = url + "agrega_estudiante"
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
# Imprimiendo la respuesta obtenida
print(post_response.text)