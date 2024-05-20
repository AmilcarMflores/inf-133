import requests

BASE_URL = "http://localhost:5000/api"

headers = {"Content-Type": "application/json"}

# # Crear un nuevo libro
# url = f'{BASE_URL}/books'
# nuevo_libro = {"title": "1984", "author": "George Orwell", "edition": "Quinta", "available": 3}
# response = requests.post(url, json=nuevo_libro, headers=headers)
# print("Creando un nuevo libro:")
# print(response.json())

# # Crear el segundo libro
# segundo_libro = {"title": "El principito", "author": "Antonie", "edition": "Primera", "available": 2}
# response = requests.post(url, json=segundo_libro, headers=headers)
# print("\nCreando el segundo libro:")
# print(response.json())

# Obtener la lista de todos los libros
url = f'{BASE_URL}/books'
response = requests.get(url, headers=headers)
print("\nLista de libros:")
print(response.json())

# # Obtener un libro específico por su id (por ejemplo, id=1)
# url = f'{BASE_URL}/books/1'
# response = requests.get(url, headers=headers)
# print("\nDetalles del libro con id: 1")
# print(response.json())

# # Actualizar un libro existente por su id (por ejemplo, id=1)
# url = f'{BASE_URL}/books/1'
# datos_actualizados = {"title": "Noches blancas", "author": "Fiodor", "edition": "Tercera", "available": 10}
# response = requests.put(url, json=datos_actualizados, headers=headers)
# print("\nActualizando el libro con id: 1")
# print(response.json())

# # Eliminar un libro existente por su id (por ejemplo, id=1)
# url = f'{BASE_URL}/books/1'
# response = requests.delete(url, headers=headers)
# print("\nEliminando el libro con id: 1")
# if response.status_code == 204:
#   print("Libro con id 1 eliminado con éxito :)")
# else:
#   print(f'Error: {response.status_code} - {response.text}')