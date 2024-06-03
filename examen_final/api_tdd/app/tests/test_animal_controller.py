# Cada test funciona de manera independiente

# Prueba para verificar la obtención de la lista de animales
def test_get_animals(test_client, auth_headers):
    # Enviamos una solicitud GET a la ruta de animales con los encabezados de autorización
    response = test_client.get("/api/animals", headers=auth_headers)
    # Verificamos que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verificamos que la respuesta sea una lista vacía (sin animales inicialmente)
    assert response.json == []

# Prueba para verificar la creación de un nuevo animal
def test_create_animal(test_client, auth_headers):
    # Creamos un diccionario con los datos del nuevo animal
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    # Enviamos una solicitud POST a la ruta de animales con los datos del nuevo animal en formato JSON y los encabezados de autorización
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    # Verificamos que el código de estado de la respuesta sea 201 (Created)
    assert response.status_code == 201
    # Verificamos que el nombre del animal en la respuesta sea "Lion"
    assert response.json["name"] == "Lion"

# Prueba para verificar la obtención de un animal específico
def test_get_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora obtén el animal
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Tiger"

# Prueba para verificar la actualización de un animal
def test_update_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora actualiza el animal
    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(f"/api/animals/{animal_id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    assert response.json["species"] == "Loxodonta africana"
    assert response.json["age"] == 12

# Prueba para verificar la eliminación de un animal
def test_delete_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora elimina el animal
    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 204

    # Verifica que el animal ha sido eliminado
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 404

# test rol user:
def test_get_animals(test_client,auth_headers_user):
    response = test_client.get("/api/animals", headers=auth_headers_user)
    assert response.status_code == 200
    assert response.json == []
    
def test_get_animal(test_client, auth_headers_user,auth_headers):
    data = {"name": "Tiger", "species": "Panthere tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]
    
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers_user)
    assert response.status_code == 200
    assert response.json["name"] == "Tiger"    
    
def test_create_animal(test_client,auth_headers_user):
    data = {"name": "Lion", "species": "Panthera leo", "age":5}
    response = test_client.post("/api/animals", json=data, headers=auth_headers_user)
    assert response.status_code == 403
    
def test_update_animal(test_client, auth_headers, auth_headers_user):
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]
    
    
    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(
        f"/api/animals/{animal_id}", json=update_data, headers=auth_headers_user
    )
    assert response.status_code == 403

def test_delete_animal(test_client,auth_headers,auth_headers_user):
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]
    
    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers_user)
    assert response.status_code == 403
    
