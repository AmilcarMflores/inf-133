from flask import Flask
from database import db
from controllers.book_controller import book_bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Configura la url de la documentación OpenAPI
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"
# Inicializa el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
  SWAGGER_URL, API_URL, config={"app_name": "Biblioteca API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la db
db.init_app(app)

# Registra el blueprint de libro en la aplicación
app.register_blueprint(book_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
  db.create_all()
  
# Ejecuta la aplicación
if __name__ == "__main__":
  app.run(debug=True)

