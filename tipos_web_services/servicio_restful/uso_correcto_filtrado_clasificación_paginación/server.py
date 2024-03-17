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
  def response_handler(self, status, data):
    self.send_response(status)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(data).encode("utf-8"))
  
  def find_student(self, id):
    return next(
        (estudiante for estudiante in estudiantes if estudiante["id"] == id),
        None,
      )
    
  def read_data(self):
    content_length = int(self.headers["Content-Length"])
    data = self.rfile.read(content_length)
    data = json.loads(data.decode("utf-8"))
    return data
  
  # Método para manejar solicitudes GET
  def do_GET(self):
    if self.path == '/estudiantes':
      self.response_handler(200, estudiantes)
    #Diseño de URL con patrones lógicos y jerarquía
    elif self.path.startswith("/estudiantes/"):
      id = int(self.path.split("/")[-1])
      estudiante = self.find_student(id)
      if estudiante:
        self.response_handler(200, [estudiante])
      else:
        self.response_handler(204, [])
    else:
      self.response_handler(404, {"Error" "Ruta no existente"})
  
  #Uso sustantivos y nombres en plural
  def do_POST(self):
    if self.path == "/estudiantes":
      data = self.read_data()
      data["id"] = len(estudiantes) + 1
      estudiantes.append(data)
      self.response_handler(201, estudiantes)
    else:
      self.response_handler(404, {"Error": "Ruta no existente"})

  #Uso correcto de filtrado, clasificación y paginación
  def do_PUT(self):
    if self.path.startswith("/estudiantes/"):
      id = int(self.path.split("/")[-1])
      estudiante = self.find_student(id)
      data = self.read_data()
      if estudiante:
        estudiante.update(data)
        self.response_handler(200, [estudiantes])
      else:
        self.response_handler(200, [estudiantes])
    else:
      self.response_handler(404, {"Error": "Ruta no existente"})
  
  def do_DELETE(self):
    if self.path == '/estudiantes':
      estudiantes.clear()
      self.response_handler(200, estudiantes)
    elif self.path.startswith("/estudiantes/"):
      id = int(self.path.split("/")[-1])
      estudiante = self.find_student(id)
      if estudiante:
        estudiantes.remove(estudiante)
        self.response_handler(200, estudiantes)
      else:
        self.response_handler(404, {"Error": "Estudiante no encontrado"})
    else:
      self.response_handler(404, {"Error": "Ruta no existente"})

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
  