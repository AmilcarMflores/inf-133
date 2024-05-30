from flask import Flask
from controllers.animal_controller import animal_bp
from database import db
from flask_swagger_ui import get_swaggerui_blueprint

from flask_jwt_extended import JWTManager
from controllers.user_controller import user_bp

app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config["JWT_SECRET_KEY"] = "tu_clave_secreta_aqui"
# Configura la url de la documentación OpenAPI
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"

# Inicializa el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
  SWAGGER_URL, API_URL, config={"app_name": "Zoológico API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Configuración de la bd
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zoo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la db
db.init_app(app)

# Inicializa la extensión JWTManager
jwt = JWTManager(app)

# Registra los blueprints de animales y usuarios en la aplicación
app.register_blueprint(animal_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
  db.create_all()
  
# Ejecuta la aplicación
if __name__ == "__main__":
  app.run(debug=True)