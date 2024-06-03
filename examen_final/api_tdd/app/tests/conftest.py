import pytest
from flask_jwt_extended import create_access_token
from app.database import db
from app.run import app


@pytest.fixture(scope="module")
# Configura un cliente de pruebas para tu aplicación Flask.
def test_client():
    # Activar el modo de prueba de Flask
    app.config["TESTING"] = True
    # Configurar la base de datos para usar SQLite en memoria (temporal)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    # Configurar una clave secreta para JWT (usada para generar y verificar tokens)
    app.config["JWT_SECRET_KEY"] = "test_secret_key"

    # Crear un cliente de pruebas para la aplicación Flask
    with app.test_client() as testing_client:
        # Iniciar el contexto de la aplicación
        with app.app_context():
            # Crear todas las tablas en la base de datos (inicialización)
            db.create_all()
            # Devolver el cliente de pruebas para ser usado en las pruebas
            yield testing_client
            # Eliminar todas las tablas de la base de datos (limpieza)
            db.drop_all()



@pytest.fixture(scope="module")
# Genera un token de autorización para las pruebas.
def auth_headers():
    # Iniciar el contexto de la aplicación
    with app.app_context():
        # Crear un token de acceso JWT con la identidad de prueba
        access_token = create_access_token(
            identity={"username": "testuser", "roles": '["admin"]'}
        )
        # Crear encabezados HTTP con el token de acceso
        headers = {"Authorization": f"Bearer {access_token}"}
        # Devolver los encabezados de autorización para ser usados en las pruebas
        return headers

# test rol user:
@pytest.fixture(scope="module")
def auth_headers_user():
    access_token = create_access_token(
        identity={"username": "testuser", "roles": '["user"]'}
    )
    headers = {"Authorization": f"Bearer {access_token}"}
    return headers