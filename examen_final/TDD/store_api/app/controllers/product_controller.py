from flask import Blueprint, request, jsonify
from models.product_model import Producto
from views.product_view import render_product_detail, render_product_list
from utils.decorators import jwt_required, roles_required
from functools import wraps

product_bp = Blueprint("product",__name__)

@product_bp.route("/products", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_products():
    products = Producto.get_all()
    return jsonify(render_product_list(products))

@product_bp.route("/products/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_product(id):
  product = Producto.get_by_id(id)
  if product:
    return jsonify(render_product_detail(product))
  return jsonify({"error": "Producto no encontrado"}), 404

@product_bp.route("/products", methods=["POST"])
@jwt_required
@roles_required(roles=["admin","user"])
def create_product():
  data = request.json
  # name, description, price, stock
  name = data.get("name")
  description = data.get("description")
  price = data.get("price")
  stock = data.get("stock")
  
  if not (name and description and price and stock):
    return jsonify({"error": "Faltan datos requeridos"}), 400
  
  product = product(name=name,description=description,price=price,stock=stock)
  product.save()
  
  return jsonify(render_product_detail(product)), 201

@product_bp.route("/products/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_product(id):
  product = product.get_by_id(id)
  
  if not product:
    return jsonify({"error": "Producto no encontrado"}), 404
  # name, description, price, stock
  name = request.json
  description = data.get("description")
  price = data.get("price")
  stock = data.get("stock")
  origin = data.get("origin")
  
  product.update(brand=brand,weight=weight,flavor=flavor,origin=origin)
  return jsonify(render_product_detail(product))

@product_bp.route("/products/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_product(id):
  product = product.get_by_id(id)
  if not product:
    return jsonify({"error": "Dulce no encontrado"}), 404
  product.delete()
  return "", 204
