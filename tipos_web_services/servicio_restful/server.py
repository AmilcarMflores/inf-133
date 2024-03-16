#Creamos un servidor REST
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

#¿Dónde almacenaremos la información?
estudiantes = [
  {
    "id":1,
    "nombre": "Pedrito",
    "apellido": "García",
    "carrera": "Ingeniería de Sistemas",
  },
]
#¿Dóndo vivirán nuestros servicios?
# Definición de una clase que maneja las solicitudes HTTP
class RESTRequestHandler(BaseHTTPRequestHandler):
  # Método para manejar solicitudes GET
  def do_GET(self):
    # Si la ruta es '/lista_estudiantes'
    if self.path == '/estudiantes':
      # Se envía una respuesta exitosa (código 200)
      self.send_response(200)
      # Se envía un encabezado indicando que el tipo de contenido es JSON
      self.send_header('Content-type', 'application/json')
      self.end_headers()
      # Se envía la lista de estudiantes como respuesta
      self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
    #Diseño de URL con patrones lógicos y jerarquía
    elif self.path.startswith("/estudiantes/"):
      id = int(self.path.split("/")[-1])
      estudiante = next(
        (estudiante for estudiante in estudiantes if estudiante["id"] == id),
        None,
      )
      if estudiante:
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(estudiante).encode("utf-8"))
    else:
      # Si la ruta no existe, se envía una respuesta de error (código 404)
      self.send_response(404)
      self.send_header('Content-type','application/json')
      self.end_headers()
      # Se envía un mensaje de error en formato JSON
      self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
  
  # Método para manejar solicitudes POST
  #Uso sustantivos y nombres en plural
  def do_POST(self):
    # Si la ruta es 
    if self.path == '/estudiantes':
      # Se lee la longitud del contenido del mensaje POST
      content_length = int(self.headers['Content-Length'])
      # Se lee el contenido del mensaje POST y se carga como JSON
      post_data = self.rfile.read(content_length)
      post_data = json.loads(post_data.decode('utf-8'))
      # Se asigna un ID al estudiante y se agrega a la lista de estudiantes
      post_data['id'] = len(estudiantes) + 1
      estudiantes.append(post_data)
      # Se envía una respuesta indicando que se creó el estudiante (código 201)
      self.send_response(201)
      self.send_header('Content-type', 'application/json')
      self.end_headers()
      # Se envía la lista de estudiantes actualizada como respuesta
      self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
    else:
      self.send_response(404)
      self.send_header('Content-type','application/json')
      self.end_headers()
      self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
      
      
  #Uso correcto de verbos y código de estado HTTP
  def do_PUT(self):
    if self.path.startswith("/estudiantes"):
      content_length = int(self.headers["Content-Length"])
      data = self.rfile.read(content_length)
      data = json.loads(data.decode("utf-8"))
      id = data["id"]
      estudiante = next(
        (estudiante for estudiante in estudiantes if estudiante["id"] == id),
        None,
      )
      if estudiante:
        estudiante.update(data)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(estudiante).encode("utf-8"))
  
  def do_DELETE(self):
    if self.path == '/estudiantes':
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.end_headers()
      estudiantes.clear()
      self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
      
  
# Función para ejecutar el servidor 
def run_server(port = 8000):
    try:
      # Se define la dirección del servidor y se crea una instancia del servidor HTTP
      server_address = ('', port)
      httpd = HTTPServer(server_address, RESTRequestHandler)
      print(f'Iniciando servidor web en http://localhost:{port}/')
      # Se pone el servidor en funcionamiento de forma indefinida
      httpd.serve_forever()
    except KeyboardInterrupt:
      # En caso de interrupción por teclado, se detiene el servidor
      print('Apagando servidor web')
      httpd.socket.close()
# Bloque principal que ejecuta la función run_server si este archivo es el programa principal
if __name__ == "__main__":
  run_server()
  