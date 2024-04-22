# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask
# '__name__' es un parámetro especial que representa el nombre del módulo actual
# El objeto vive en 'app'
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.
app = Flask(__name__)

@app.route('/')
def index():
  return '¡Hola mundo!'

# Agregamos una nueva ruta
# Expresamos de forma explícita que el tipo de método HTTP es GET
@app.route('/saludar', methods=['GET'])
def saludar():
  nombre = request.args.get("nombre")
  if not nombre:
    return(
      jsonify({"error": "se requiere un nombre en los parámetros de la URL."}),
      400,
    )
  return jsonify({"mensaje": f"¡Hola, {nombre}!"})
# Esta condición verifica si este script se está ejecutando directamente.
# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == '__main__':
  app.run()


