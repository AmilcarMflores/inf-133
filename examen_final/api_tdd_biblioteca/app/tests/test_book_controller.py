#Prueba para verificar la obtención de la lista de libros:

# admin
def test_get_books(test_client, auth_headers_admin):
  response = test_client.get("/api/books", headers=auth_headers_admin)
  assert response.status_code == 200
  assert response.json == []
# user
def test_get_books(test_client, auth_headers_user):
  response = test_client.get("/api/books", headers=auth_headers_user)
  assert response.status_code == 200
  assert response.json == []
  
#Prueba para verificar la obtención de un libro específico:
# title,author,edition,available

# admin
def test_get_book(test_client, auth_headers_admin):
  data = {"title": "1984", "author": "George Orwell", "edition": "Primera", "available": 1}
  response = test_client.post("/api/books", json=data, headers=auth_headers_admin)
  assert response.status_code == 201
  book_id = response.json["id"]
  
  response = test_client.get(f"/api/books/{book_id}", headers=auth_headers_admin)
  assert response.status_code == 200
  assert response.json["title"] == "1984"
# user
def test_get_book(test_client, auth_headers_admin, auth_headers_user):
  data = {"title": "1984", "author": "George Orwell", "edition": "Primera", "available": 1}
  response = test_client.post("/api/books", json=data, headers=auth_headers_admin)
  assert response.status_code == 201
  book_id = response.json["id"]
  
  response = test_client.get(f"/api/books/{book_id}", headers=auth_headers_user)
  assert response.status_code == 200
  assert response.json["title"] == "1984"

# Prueba para verificar la creación de un nuevo libro:
# title,author,edition,available

# admin
def test_create_book(test_client, auth_headers_admin):
  data = {"title": "El principito", "author": "Antonie E.", "edition": "Segunda", "available": 10}
  response = test_client.post("/api/books", json=data, headers=auth_headers_admin)
  assert response.status_code == 201
  assert response.json["title"] == "El principito"
  
# Prueba para verificiar la actualización de un libro:

# admin
def test_update_book(test_client, auth_headers_admin):
  data = {"title": "El viejo y el mar", "author": "Ernest H.", "edition": "Quinta", "available": 20}
  response = test_client.post(f"/api/books", json=data, headers=auth_headers_admin)
  assert response.status_code == 201
  book_id = response.json["id"]

  update_data = {"title": "El viejo y el mar", "author": "Ernest H.", "edition": "Sexta", "available": 4}
  response = test_client.put(f"/api/books/{book_id}", json=update_data, headers=auth_headers_admin)
  assert response.status_code == 200
  assert response.json["edition"] == "Sexta"
  assert response.json["available"] == 4 
  
# Prueba para verificar la eliminación de un libro
# title,author,edition,available

# admin
def test_delete_book(test_client, auth_headers_admin):
  data = {"title": "El mundo de Sofía", "author": "Jostein Gaarder", "edition": "Quinta", "available": 2}
  response = test_client.post("/api/books", json=data, headers=auth_headers_admin)
  assert response.status_code == 201
  book_id = response.json["id"]
  
  response = test_client.delete(f"/api/books/{book_id}", headers=auth_headers_admin)
  assert response.status_code == 204
  
  response = test_client.get(f"/api/books/{book_id}", headers=auth_headers_admin)
  assert response.status_code == 404