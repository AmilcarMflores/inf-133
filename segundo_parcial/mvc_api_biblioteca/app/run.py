from flask import Flask
from controllers.libro_contoller import book_bp
from database import db

app = Flask(__name__)

# Configuración de db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la bd
db.init_app(app)

# Registra el blueprint de libros en la aplicación
app.register_blueprint(book_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
  db.create_all()
  
# Ejecuta la aplicación
if __name__ == "__main__":
  app.run(debug=True)