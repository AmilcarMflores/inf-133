# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask
# '__name__' es un parámetro especial que representa el nombre del módulo actual
# El objeto vive en 'app'
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.
app = Flask(__name__)

# Define una función para manejar solicitudes GET en la ruta raíz ('/')
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

# Ejercicios
# Suma de dos números
@app.route('/sumar')
def sumar():
  numero_uno = request.args.get('num1')
  numero_dos = request.args.get('num2')
  if not numero_uno:
    return(
      jsonify({"error": "se requiere el primer número, para sumar, en los parámetros de la URL..."})
    )
  elif not numero_dos:
    return(
      jsonify({"error": "se requiere el segundo número, para sumar, en los parámetros de la URL"})
    )
  numero_uno_int = int(numero_uno)
  numero_dos_int = int(numero_dos)  
  suma = numero_uno_int + numero_dos_int
  return jsonify({"mensaje": f"La suma de {numero_uno} con {numero_dos} es: {suma}."})

# Determina si una cadena es palindromo
@app.route('/palindromo')
def es_palindromo():
  cadena = request.args.get('cadena')
  if not cadena:
    return(jsonify({"error": "se requiere una palabra, para comprobar si es palíndromo, en los parámetros de la URL..."}))
  cadena_invertida = cadena[::-1]
  if cadena == cadena_invertida:
    return (jsonify({"mensaje": f"La palabra {cadena} es palíndromo: {cadena_invertida}"}))
  else:
    return (jsonify({"mensaje": f"La palabra {cadena} no es palíndromo: {cadena_invertida}"}))
  
# Cuenta una vocal en una cadena
@app.route('/contar')
def contar_vocales():
  cadena = request.args.get('cadena')
  vocal = request.args.get('vocal')
  if not cadena or not vocal:
    return(jsonify({"mensaje": "se requiere una palabra y una vocal, en los parámetros de la URL..."}))
  contar = cadena.count(vocal)
  return(jsonify({"mensaje": f"La palabra {cadena} tiene: {contar} vocales {vocal}"}))
  
# Esta condición verifica si este script se está ejecutando directamente.
# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == '__main__':
  app.run()


