import requests

# URL
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo libro
url = f"{BASE_URL}/books"
nuevo_libro = {"title": "1984", "author": "George Orwell", "edition": 1, "availability": 5}
response = requests.post(url, json=nuevo_libro, headers=headers)
print("Creando un nuevo libro :)")
print(response.json())

# # Crear el segundo libro
# libro_dos = {"title": "El viejo y el mar", "author": "Ernest Hemingway", "edition": 2, "availability": 12}
# response = requests.post(url, json=libro_dos, headers=headers)
# print("\nCreando el segundo libro:")
# print(response.json())

# Obtener la lista de todos los libros
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print("\nLista de libros:")
print(response.json())

# # Obtener un libro por su id
# url = f"{BASE_URL}/books/1"
# response = requests.get(url, headers=headers)
# print("\nDetaller del libro con id 1:")
# print(response.json())

# # Actualizar un libro existente por su id 
# url = f"{BASE_URL}/books/1"
# datos_actualizados = {"title": "Borracho estaba, pero me acuerdo", "author": "Victor Hugo Viscarra", "edition": 3, "availability": 25}
# response = requests.put(url, json=datos_actualizados, headers=headers)
# print("\nActualizando el libro con id 1:")
# print(response.json())

# # Eliminar un libro existente por su id
# url = f"{BASE_URL}/books/1"
# response = requests.delete(url, headers=headers)
# print("\nEliminando el libro con id 1:")
# if response.status_code == 204:
#   print(f"Libro con id 1 eliminando con éxito")
# else:
#   print(f"Error: {response.status_code} - {response.text}")