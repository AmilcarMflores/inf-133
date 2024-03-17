import requests

url = "http://localhost:8000/"

# Realizando una solicitud GET a la ruta /lista_estudiantes del servidor local
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
# Imprimiendo la respuesta obtenida
print(get_response.text)

# Creando un nuevo estudiante para agregar al servidor
nuevo_estudiante = {
  "nombre": "Juanito",
  "apellido": "Pérez",
  "carrera": "Ingenieria Agronómica",
}
# Realizando una solicitud POST para agregar un nuevo estudiante a la ruta /estudiantes del servidor local
ruta_post = url + "estudiantes"
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
# Imprimiendo la respuesta obtenida
print(post_response.text)

#GET busca a un estudiante por id /estudiantes/{id}
ruta_filtrar_nombre = url + "estudiantes/1"
filtrar_nombre_response = requests.request(method="GET", url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)

#PUT actualiza un estudiante por la ruta /estudiantes
ruta_actualizar = url + "estudiantes"
estudiante_actualizado = {
  "id": 1,
  "nombre": "Juan",
  "apellido": "Pérez",
  "carrera": "Ingeniería Agronómica",
}
put_response = requests.request(
  method="PUT", url=ruta_actualizar, json=estudiante_actualizado
)
print(put_response.text)

#DELETE elimina todos los estudiantes por la ruta /estudiantes
ruta_eliminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", url=ruta_eliminar)
print(eliminar_response.text)



