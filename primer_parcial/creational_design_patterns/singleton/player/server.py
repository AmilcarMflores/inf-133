from http.server import BaseHTTPRequestHandler, HTTPServer  # Importa clases para crear el servidor HTTP y manejar solicitudes HTTP.
import json  # Importa el módulo JSON para trabajar con datos JSON.

# Clase Player utilizando el patrón Singleton
class Player:
    _instance = None  # Variable de clase que mantendrá la instancia única.

    def __new__(cls, name):  # Método para controlar la creación de nuevas instancias.
        if not cls._instance:  # Si aún no hay una instancia.
            cls._instance = super().__new__(cls)  # Crea una nueva instancia.
            cls._instance.name = name  # Inicializa el nombre del jugador.
            cls._instance.health = 100  # Inicializa la salud del jugador.
        return cls._instance  # Retorna la instancia única.       
    
    def take_damage(self, damage):
      self.health -= damage
      if self.health < 0:
        self.health = 0
        
    def to_dict(self):  # Método para convertir los datos del jugador a un diccionario.
        return {"name": self.name, "health": self.health}  # Retorna los datos como diccionario.


# Manejador de solicitudes HTTP para el jugador
class PlayerHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # Maneja las solicitudes GET.
        if self.path == "/player":  # Si la ruta es "/player".
            self.send_response(200)  # Envía una respuesta HTTP 200 (OK).
            self.send_header("Content-type", "application/json")  # Establece el tipo de contenido como JSON.
            self.end_headers()  # Finaliza los encabezados de la respuesta.
            player_data = json.dumps(player.to_dict())  # Convierte los datos del jugador a JSON.
            self.wfile.write(player_data.encode("utf-8"))  # Escribe los datos JSON en el cuerpo de la respuesta.
        else:
            self.send_response(404)  # Envía una respuesta HTTP 404 (No encontrado).
            self.end_headers()  # Finaliza los encabezados de la respuesta.
    
    def do_POST(self):
        if self.path == "/player/damage":
          content_length = int(self.headers['Content-Length'])
          post_data = self.rfile.read(content_length)
          data =json.loads(post_data.decode('utf-8'))
          damage = data.get("damage", 0)
          player.take_damage(damage)
          self.send_response(200)
          self.send_header("Content-type", "application/json")
          self.end_headers()
          player_data = json.dumps(player.to_dict())
          self.wfile.write(player_data.encode("utf-8"))
        else:
          self.send_response(404)
          self.end_headers()

def main():  # Función principal para iniciar el servidor.
    global player  # Declara la variable global 'player'.
    player = Player("Alice")  # Crea la instancia del jugador con el nombre "Alice".

    try:
        server_address = ("", 8000)  # Configura la dirección del servidor y el puerto.
        httpd = HTTPServer(server_address, PlayerHandler)  # Crea una instancia de HTTPServer con la dirección y el manejador de solicitudes.
        httpd.serve_forever()  # Inicia el servidor para manejar solicitudes indefinidamente.
    except KeyboardInterrupt:  # Maneja la interrupción del teclado.
        print("Apagando servidor HTTP")  # Imprime un mensaje indicando que el servidor se está apagando.
        httpd.socket.close()  # Cierra el socket del servidor.

if __name__ == "__main__":  # Comprueba si este script se está ejecutando como el programa principal.
    main()  # Llama a la función principal para iniciar el servidor.
