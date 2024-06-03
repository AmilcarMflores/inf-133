import requests  # Importa el módulo requests para realizar solicitudes HTTP.

# URL del servidor y cabeceras para las solicitudes
url = "http://localhost:8000/delivery"  # URL del endpoint de entrega en el servidor.
headers = {"Content-Type": "application/json"}  # Cabeceras de la solicitud indicando que el contenido es JSON.

# Primer vehículo: motorcycle
vehicle_type = "motorcycle"  # Define el tipo de vehículo como "motorcycle".
data = {"vehicle_type": vehicle_type}  # Crea el cuerpo de la solicitud con el tipo de vehículo.
response = requests.post(url, json=data, headers=headers)  # Envía la solicitud POST al servidor con los datos JSON y las cabeceras.
if response.status_code == 201:  # Verifica si el código de estado de la respuesta es 201 (Creado).
    print(response.text)  # Imprime el texto de la respuesta.
else:
    print("Error programando entrega:", response.text)  # Imprime un mensaje de error si el estado no es 201.

# Segundo vehículo: drone
vehicle_type = "drone"  # Define el tipo de vehículo como "drone".
data = {"vehicle_type": vehicle_type}  # Crea el cuerpo de la solicitud con el tipo de vehículo.
response = requests.post(url, json=data, headers=headers)  # Envía la solicitud POST al servidor con los datos JSON y las cabeceras.
if response.status_code == 201:  # Verifica si el código de estado de la respuesta es 201 (Creado).
    print(response.text)  # Imprime el texto de la respuesta.
else:
    print("Error programando entrega:", response.text)  # Imprime un mensaje de error si el estado no es 201.

# Tercer vehículo: scout
vehicle_type = "scout"  # Define el tipo de vehículo como "scout".
data = {"vehicle_type": vehicle_type}  # Crea el cuerpo de la solicitud con el tipo de vehículo.
response = requests.post(url, json=data, headers=headers)  # Envía la solicitud POST al servidor con los datos JSON y las cabeceras.
if response.status_code == 201:  # Verifica si el código de estado de la respuesta es 201 (Creado).
    print(response.text)  # Imprime el texto de la respuesta.
else:
    print("Error programando entrega:", response.text)  # Imprime un mensaje de error si el estado no es 201.
