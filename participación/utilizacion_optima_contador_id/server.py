from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de pizzas
pizzas = {}

# Producto: Pizza
class Pizza:
    def __init__(self):
        self.tamaño = None
        self.masa = None
        self.toppings = []

    def __str__(self):
        return f"Tamaño: {self.tamaño}, Masa: {self.masa}, Toppings: {', '.join(self.toppings)}"


# Builder: Constructor de pizzas
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_tamaño(self, tamaño):
        self.pizza.tamaño = tamaño

    def set_masa(self, masa):
        self.pizza.masa = masa

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)

    def get_pizza(self):
        return self.pizza


# Director: Pizzería
class Pizzeria:
    def __init__(self, builder):
        self.builder = builder

    def create_pizza(self, tamaño, masa, toppings):
        self.builder.set_tamaño(tamaño)
        self.builder.set_masa(masa)
        for topping in toppings:
            self.builder.add_topping(topping)
        return self.builder.get_pizza()

# Aplicando el principio de responsabilidad única (S de SOLID)
class PizzaService:
    def __init__(self):
        self.builder = PizzaBuilder()
        self.pizzeria = Pizzeria(self.builder)
        
    global pizza_counter  
    pizza_counter = 0 #Contador para asignar identificadores
      
    def create_pizza(self, post_data):
        tamaño = post_data.get("tamaño", None)
        masa = post_data.get("masa", None)
        toppings = post_data.get("toppings", [])

        pizza = self.pizzeria.create_pizza(tamaño, masa, toppings)
        #pizzas[len(pizzas) + 1] = pizza
        # Incrementar el contador global
        global pizza_counter
        pizza_counter += 1
        pizzas[pizza_counter] = pizza
        return pizza
      
    def read_pizzas(self):
        return {index: pizza.__dict__ for index, pizza in pizzas.items()}
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


# Manejador de solicitudes HTTP
class PizzaHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.controller = PizzaService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/pizzas":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.controller.create_pizza(data)
            HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_GET(self):
        if self.path == "/pizzas":
            response_data = self.controller.read_pizzas()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

def run(server_class=HTTPServer, handler_class=PizzaHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()