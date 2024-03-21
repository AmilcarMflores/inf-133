from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation

class Estudiante(ObjectType):
  id = Int()
  nombre = String()
  apellido = String()
  carrera = String()

class Query(ObjectType):
  estudiantes = List(Estudiante)
  estudiante_por_id = Field(Estudiante, id=Int())
  
  def resolve_estudiantes(root, info):
    return estudiantes
  
  def resolver_estudiante_por_id(root, info, id):
    for estudiante in estudiantes:
      if estudiante.id == id:
        return estudiante
    return None
  
estudiantes = [
  Estudiante(
    id = 1, nombre = "Pedrito", apellido = "Garcia", carrera = "Ingeniería en Sistemas"
  ),
  Estudiante(
    id = 2, nombre = "José", apellido = "Lopez", carrera = "Arquitectura"
  ),
]

#Creando un nuevo estudiante
class CrearEstudiante(Mutation):
  class Arguments:
    nombre = String()
    apellido = String()
    carrera = String()
    
  estudiante = Field(Estudiante)

  def mutate(root, info, nombre, apellido, carrera):
    nuevo_estudiante = Estudiante(
      id = len(estudiantes) + 1,
      nombre = nombre,
      apellido = apellido,
      carrera = carrera
    )
    estudiantes.append(nuevo_estudiante)
    return CrearEstudiante(estudiante = nuevo_estudiante)

class Mutations(ObjectType):
  crear_estudiante = CrearEstudiante.Field()

schema = Schema(query = Query, mutation = Mutations)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            print(data)
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()