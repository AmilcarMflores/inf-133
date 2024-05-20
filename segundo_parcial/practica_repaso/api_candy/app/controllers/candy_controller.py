from flask import Blueprint, request, jsonify
from models.candy_model import Dulce
from views.candy_view import render_dulce_detail, render_dulce_list
from utils.decorators import jwt_required, roles_required

dulce_bp = Blueprint("dulce", __name__)

@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_dulces():
    dulces = Dulce.get_all()
    return jsonify(render_dulce_list(dulces))


@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_dulce(id):
    dulce = Dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "Dulce no encontrado"}), 404

@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_dulce():
    data = request.json
    marca = data.get("marca")
    peso = data.get("peso")
    sabor = data.get("sabor")
    origen = data.get("origen")

    if not marca or peso is None or not sabor or not origen:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    dulce = Dulce(marca=marca, peso=peso, sabor=sabor, origen=origen)
    dulce.save()

    return jsonify(render_dulce_detail(dulce)), 201

