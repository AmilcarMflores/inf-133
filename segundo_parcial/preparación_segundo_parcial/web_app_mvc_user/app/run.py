from flask import Flask
from flask_login import LoginManager

from controllers import user_controller

from database import db
from models.user_model import User

app = Flask(__name__)
# Configuración de la db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODFICATIONS"] = False
app.config["SECRET_KEY"] = "clave-secreta"
# Configuración de Flask-Login
login_manager = LoginManager()
# Especifica la ruta de inicio de sesión
login_manager.login_view = "user.login"
login_manager.init_app(app)

# Función para cargar un usuario basado en su id
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# Inicializa db con la aplicación Flask
db.init_app(app)
# Registra el blueprint de usuarios
app.register_blueprint(user_controller.user_bp)

if __name__ == "__main__":
  # Crea las tablas si no existen
  with app.app_context():
    db.create_all()
  app.run(debug=True)