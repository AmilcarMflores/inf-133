from http.server import HTTPServer, BaseHTTPRequestHandler  # Importa clases para crear el servidor HTTP y manejar solicitudes HTTP básicas.
import json  # Importa el módulo JSON para trabajar con datos JSON.

# Clase base para los vehículos de entrega
class DeliveryVehicle:
    def __init__(self, capacity):  # Constructor que inicializa la capacidad y el contador de entregas realizadas.
        self.capacity = capacity  # Capacidad máxima de entregas del vehículo.
        self.packages_delivered = 0  # Contador de entregas realizadas.

    def deliver(self):  # Método para realizar una entrega.
        if self.packages_delivered < self.capacity:  # Comprueba si aún puede realizar entregas.
            self.packages_delivered += 1  # Incrementa el contador de entregas realizadas.
            return "Entrega realizada con éxito"  # Retorna un mensaje de éxito.
        else:
            return "El vehículo ha alcanzado su capacidad máxima de entregas"  # Retorna un mensaje de capacidad máxima alcanzada.

# Clase Motorcycle que hereda de DeliveryVehicle
class Motorcycle(DeliveryVehicle):
    def __init__(self):  # Constructor que llama al constructor de la clase base con una capacidad específica.
        super().__init__(capacity=10)  # Establece la capacidad de la motocicleta a 10.

# Clase Drone que hereda de DeliveryVehicle
class Drone(DeliveryVehicle):
    def __init__(self):  # Constructor que llama al constructor de la clase base con una capacidad específica.
        super().__init__(capacity=20)  # Establece la capacidad del dron a 20.

# Clase Scout que hereda de DeliveryVehicle
class Scout(DeliveryVehicle):
    def __init__(self):  # Constructor que llama al constructor de la clase base con una capacidad específica.
        super().__init__(capacity=5)  # Establece la capacidad del scout a 5.

# Fábrica de vehículos de entrega
class DeliveryFactory:
    def create_delivery_vehicle(self, vehicle_type):  # Método para crear un vehículo de entrega según el tipo.
        if vehicle_type == "motorcycle":  # Comprueba si el tipo de vehículo es "motorcycle".
            return Motorcycle()  # Retorna una instancia de Motorcycle.
        elif vehicle_type == "drone":  # Comprueba si el tipo de vehículo es "drone".
            return Drone()  # Retorna una instancia de Drone.
        elif vehicle_type == "scout":  # Comprueba si el tipo de vehículo es "scout".
            return Scout()  # Retorna una instancia de Scout.
        else:
            raise ValueError("Tipo de vehículo de entrega no válido")  # Lanza un error si el tipo de vehículo no es válido.

# Manejador de datos HTTP
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):  # Envía una respuesta HTTP con el estado y los datos dados.
        handler.send_response(status)  # Envía el código de estado HTTP.
        handler.send_header("Content-Type", "application/json")  # Establece el tipo de contenido como JSON.
        handler.end_headers()  # Finaliza los encabezados de la respuesta.
        handler.wfile.write(json.dumps(data).encode("utf-8"))  # Escribe los datos JSON en el cuerpo de la respuesta.

    @staticmethod
    def handle_reader(handler):  # Lee y devuelve los datos del cuerpo de la solicitud POST.
        content_length = int(handler.headers["Content-Length"])  # Obtiene la longitud del contenido de la solicitud.
        post_data = handler.rfile.read(content_length)  # Lee los datos del cuerpo de la solicitud.
        return json.loads(post_data.decode("utf-8"))  # Decodifica los datos JSON y los retorna como un diccionario de Python.

# Manejador de solicitudes de entrega
class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):  # Constructor que inicializa la fábrica de vehículos de entrega.
        self.delivery_factory = DeliveryFactory()  # Crea una instancia de DeliveryFactory.
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base.

    def do_POST(self):  # Maneja las solicitudes POST.
        if self.path == "/delivery":  # Comprueba si la ruta de la solicitud es "/delivery".
            data = HTTPDataHandler.handle_reader(self)  # Lee los datos de la solicitud.
            vehicle_type = data.get("vehicle_type")  # Obtiene el tipo de vehículo del cuerpo de la solicitud.
            delivery_vehicle = self.delivery_factory.create_delivery_vehicle(vehicle_type)  # Crea el vehículo de entrega correspondiente.
            response_data = {"message": delivery_vehicle.deliver()}  # Realiza una entrega y prepara los datos de la respuesta.
            HTTPDataHandler.handle_response(self, 201, response_data)  # Envía la respuesta con un estado 201 (Creado).
        else:
            HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})  # Responde con 404 si la ruta no es encontrada.

# Función principal para iniciar el servidor
def main():
    try:
        server_address = ("", 8000)  # Configura la dirección del servidor y el puerto.
        httpd = HTTPServer(server_address, DeliveryRequestHandler)  # Crea una instancia de HTTPServer con la dirección y el manejador de solicitudes.
        print("Iniciando servidor HTTP en puerto 8000...")  # Imprime un mensaje indicando que el servidor está iniciando.
        httpd.serve_forever()  # Inicia el servidor para manejar solicitudes indefinidamente.
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")  # Imprime un mensaje indicando que el servidor se está apagando.
        httpd.socket.close()  # Cierra el socket del servidor.

if __name__ == "__main__":  # Comprueba si este script se está ejecutando como el programa principal.
    main()  # Llama a la función principal para iniciar el servidor.
