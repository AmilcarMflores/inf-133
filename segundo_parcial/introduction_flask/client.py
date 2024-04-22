import requests

# URL del servidor Flask
url = 'http://localhost:5000/'

# Realizar una solicitud GET al servidor Flask
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
  print("Respuesta del servidor:")
  print(response.text)
else:
  print("Error al conectar con el servidor:", response.status_code)

# Método GET: obtener un saludo proporcionando el nombre como parámetro en la url
params = {'nombre': 'Robocop'}
response = requests.get(url + 'saludar', params = params)  

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
  data = response.json()
  mensaje = data['mensaje']
  print("Respuesta del servidor (GET):", mensaje)
else:
  print("Error al conectar con el servidor (GET):", response.status_code)

#Ejercicios
# Agrega las siguiente rutas y consume desde el cliente
# Suma dos numeros:
# ● /sumar?num1=5&num2=3
# Determina si una cadena es palindromo
# ● /palindromo?cadena=”reconocer”
# Cuenta una vocal en una cadena
# ● /contar?cadena=”exepciones”&vocal=”e”
