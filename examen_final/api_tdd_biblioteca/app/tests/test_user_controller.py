# Prueba para verificar el registro de un nuevo usuario
def test_register_user(test_client):
  new_user = {"username": "testuser", "password": "testpassword"}
  response = test_client.post("/api/register", json=new_user)
  assert response.status_code == 201
  
# Prueba para verificar el registro de un usuario duplicado
def test_register_duplicate_user(test_client):
  new_user = {"username": "testuser", "password": "testpassword"}
  response = test_client.post("/api/register", json=new_user)
  assert response.status_code == 400
  assert response.json["error"] == "El nombre de usuario ya está en uso"

# Prueba para verficar el inicio de sesión de un usuario
def test_login_user(test_client):
  user_credentials = {"username": "testuser", "password": "testpassword"}
  response = test_client.post("/api/login", json=user_credentials)
  assert response.status_code == 200