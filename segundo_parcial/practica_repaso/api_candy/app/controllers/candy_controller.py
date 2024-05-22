from flask import Blueprint, request, jsonify
from models.candy_model import Candy
from views.candy_view import render_candy_list, render_candy_detail
from utils.decorators import jwt_required, roles_required
from functools import wraps

candy_bp = Blueprint("candy",__name__)

@candy_bp.route("/candies", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_candies():
  candies = Candy.get_all()
  return jsonify(render_candy_list(candies))

@candy_bp.route("/candies/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_candy(id):
  candy = Candy.get_by_id(id)
  if candy:
    return jsonify(render_candy_detail(candy))
  return jsonify({"error": "Dulce no encontrado"}), 404

@candy_bp.route("/candies", methods=["POST"])
@jwt_required
@roles_required(roles=["admin","user"])
def create_candy():
  data = request.json
  # brand,weight,flavor,origin
  brand = data.get("brand")
  weight = data.get("weight")
  flavor = data.get("flavor")
  origin = data.get("origin")
  
  if not (brand and weight is not None and flavor and origin):
    return jsonify({"error": "Faltan datos requeridos"}), 400
  
  candy = Candy(brand=brand,weight=weight,flavor=flavor,origin=origin)
  candy.save()
  
  return jsonify(render_candy_detail(candy)), 201

@candy_bp.route("/candies/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_candy(id):
  candy = Candy.get_by_id(id)
  
  if not candy:
    return jsonify({"error": "Dulce no encontrado"}), 404
  
  data = request.json
  brand = data.get("brand")
  weight = data.get("weight")
  flavor = data.get("flavor")
  origin = data.get("origin")
  
  candy.update(brand=brand,weight=weight,flavor=flavor,origin=origin)
  return jsonify(render_candy_detail(candy))

@candy_bp.route("/candies/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_candy(id):
  candy = Candy.get_by_id(id)
  if not candy:
    return jsonify({"error": "Dulce no encontrado"}), 404
  candy.delete()
  return "", 204