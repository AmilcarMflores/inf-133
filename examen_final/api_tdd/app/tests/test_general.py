
def test_index(test_client):
    response = test_client.get("/")
    # Verificar assert(comparación lógica)
    assert response.status_code == 404

# verficamos que se levante el swagger:
def test_swagger_ui(test_client):
    # verificar --> get
    response = test_client.get("/api/docs/")
    assert response.status_code == 200
    # verficamos que la página sí sea swagger:
    # la cadena "id=swagger-ui" esté dentro de data
    assert b'id="swagger-ui"' in response.data
