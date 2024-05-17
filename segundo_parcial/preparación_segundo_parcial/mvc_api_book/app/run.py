from flask import Flask
from database import db
from controllers.book_controller import book_bp

app = Flask(__name__)

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

