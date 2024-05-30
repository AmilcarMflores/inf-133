
# Prueba para verificar el índice del servidor
def test_index(test_client):
    # Enviamos una solicitud GET a la raíz del servidor
    response = test_client.get("/")
    # Verificamos que el código de estado de la respuesta sea 404 (Not Found)
    assert response.status_code == 404

# Prueba para verificar que la interfaz de Swagger se levanta correctamente
def test_swagger_ui(test_client):
    # Enviamos una solicitud GET a la ruta de la documentación de Swagger
    response = test_client.get("/api/docs/")
    # Verificamos que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verificamos que el contenido de la página incluya la cadena "id=swagger-ui"
    # Esto asegura que la página cargada es efectivamente la interfaz de Swagger
    assert b'id="swagger-ui"' in response.data
