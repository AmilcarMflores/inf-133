# Utilizando el patrón de diseño Builder caso: pizeería

# ● Necesitamos construir una API para un cadena de pizzerías que
# maneja diversos sabores según la región de su sucursal.
# ● Por ejemplo, solo en la ciudad de La Paz ofrecen pizza con charque
# de llama y solo en la ciudad de Beni tiene disponible una pizza de
# carne de yacaré
# ● Los únicos datos en común entre las pizzas son: tamaño y masa
# ● La cantidad de toppings es variable

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Pizza:
  def __init__(self):
    self.tamaño = None
    self.masa = None
    self.toppings = []
    
  def __str__(self):
    return f"Tamaño: {self.tamaño}, Masa: {self.masa}, Toppings: {', '.join(self.toppings)}"

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
    
class Pizzeria:
  def __init__(self, builder):
    self.builder = builder
  
  def create_pizza(self, tamaño, masa, toppings):
    self.builder.set_tamaño(tamaño)
    self.builder.set_masa(masa)
    for topping in toppings:
      self.builder.add_topping(topping)
    return self.builder.get_pizza()
  
class PizzaHandler(BaseHTTPRequestHandler):
  def do_POST(self):
    if self.path == '/pizza':
      content_length = int(self.headers['Content-Length'])
      post_data = self.rfile.read(content_length)
      
      data = json.loads(post_data.decode('utf-8'))
      
      tamaño = data.get('tamaño', None)
      masa = data.get('masa', None)
      toppings = data.get('toppings', [])
      
      builder = PizzaBuilder()
      pizzeria = Pizzeria(builder)
      
      pizza = pizzeria.create_pizza(tamaño, masa, toppings)
      
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.end_headers()
      
      response = {
        'tamaño': pizza.tamaño,
        'masa': pizza.masa,
        'toppings': pizza.toppings
      }
      
      self.wfile.write(json.dumps(response).encode('utf-8'))
    else:
      self.send_response(404)
      self.end_headers()

def run(server_class=HTTPServer, handler_class=PizzaHandler, port=8000):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f"Iniciando servidor HTTP en puerto {port}...")
  httpd.serve_forever()

if __name__ == '__main__':
  run()
  