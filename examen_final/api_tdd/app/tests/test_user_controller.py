
# Prueba para verificar el registro de un nuevo usuario
def test_register_user(test_client):
    # Creamos un diccionario con los datos del nuevo usuario
    new_user = {"username": "testuser", "password": "testpassword"}
    # Enviamos una solicitud POST a la ruta de registro con los datos del nuevo usuario en formato JSON
    response = test_client.post("/api/register", json=new_user)
    # Verificamos que el código de estado de la respuesta sea 201 (Created)
    assert response.status_code == 201

# Prueba para verificar el registro de un usuario duplicado
def test_register_duplicate_user(test_client):
    # Creamos un diccionario con los datos del usuario que ya existe
    new_user = {"username": "testuser", "password": "testpassword"}
    # Enviamos una solicitud POST a la ruta de registro con los datos del usuario duplicado en formato JSON
    response = test_client.post("/api/register", json=new_user)
    # Verificamos que el código de estado de la respuesta sea 400 (Bad Request)
    assert response.status_code == 400
    # Verificamos que el mensaje de error sea el esperado
    assert response.json["error"] == "El nombre de usuario ya está en uso"

# Prueba para verificar el inicio de sesión de un usuario
def test_login_user(test_client):
    # Creamos un diccionario con las credenciales del usuario
    user_credentials = {"username": "testuser", "password": "testpassword"}
    # Enviamos una solicitud POST a la ruta de inicio de sesión con las credenciales del usuario en formato JSON
    response = test_client.post("/api/login", json=user_credentials)
    # Verificamos que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
