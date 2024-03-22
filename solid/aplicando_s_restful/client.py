import requests

url = "http://localhost:8000/"

ruta_post = url + "estudiantes"
nuevo_estudiante = {
  "nombre": "Juanito",
  "apellido": "Pérez",
  "carrera": "Ingeniería Agronómica",  
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
