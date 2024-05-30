from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
import json

# El decorador jwt_required protege una función verificando que la solicitud contenga un JWT válido. Si el token es válido, la función decorada se ejecuta normalmente. Si no, se devuelve una respuesta de error con un estado 401 Unauthorized. 
def jwt_required(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    try:
      verify_jwt_in_request()
      return fn(*args, **kwargs)
    except Exception as e:
      return jsonify({"error": str(e)}), 401
    
  return wrapper
# El decorador roles_required protege una función verificando que la solicitud contenga un JWT válido y que el usuario tenga al menos uno de los roles especificados. Si el token es válido y el usuario tiene un rol permitido, la función decorada se ejecuta normalmente. Si no, se devuelve una respuesta de error con un estado 403 Forbidden (si el rol no es autorizado) o 401 Unauthorized (si hay un problema con el token JWT).
def roles_required(roles=[]):
  def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      try:
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        user_roles = json.loads(current_user.get("roles", []))
        if not set(roles).intersection(user_roles):
          return jsonify({"error": "Acceso no autorizado para este rol"}), 403
        return fn(*args, **kwargs)
      except Exception as e:
        return jsonify({"error": str(e)}), 401
    
    return wrapper
  return decorator  
  

