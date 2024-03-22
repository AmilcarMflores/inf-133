from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

estudiantes = [
  {
    "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
  },
]

class EstudiantesService:
  @staticmethod
  def add_student(data):
    data["id"] = len(estudiantes) + 1
    estudiantes.append(data)
    return estudiantes

class HTTPResponseHandler:
  @staticmethod
  def handle_response(handler, status, data):
    handler.send_response(status)
    handler.send_header("Content-type", "application/json")
    handler.end_headers()
    handler.wfile.write(json.dumps(data).encode("utf-8"))
  
class RESTRequestHandler(BaseHTTPRequestHandler):
  
      
  def do_POST(self):
    if self.path == "/estudiantes":
      data = self.read_data()
      estudiantes = EstudiantesService.add_student(data)
      HTTPResponseHandler.handle_response(self, 201, estudiantes)
    else:
      HTTPResponseHandler.handle_response(
        self, 404, {"Error": "Ruta no existente"}
      )
  
  def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data

def run_server(port=8000):
  try:
    server_address = ("", port)
    http = HTTPServer(server_address, RESTRequestHandler)
    print(f"Iniciando servidor web en https://localhost:{port}/")
    http.serve_forever()
  except KeyboardInterrupt:
    print("Apagando servidor web")
    http.socket.close()

if __name__ == "__main__":
  run_server()