from flask import Blueprint, request, jsonify
from models.book_model import Book
from views.book_view import render_book_detail, render_book_list
from utils.decorators import jwt_required, roles_required
from functools import wraps

book_bp = Blueprint("book",__name__)

@book_bp.route("/books", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_books():
  books = Book.get_all()
  return jsonify(render_book_list(books))

@book_bp.route("/books/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_book(id):
  book = Book.get_by_id(id)
  if book:
    return jsonify(render_book_detail(book))
  return jsonify({"error": "Libro no encontrado"}), 404

@book_bp.route("/books", methods=["POST"])
@jwt_required
@roles_required(roles=["admin","user"])
def create_book():
  data = request.json
  # title,author,edition,available
  title = data.get("title")
  author = data.get("author")
  edition = data.get("edition")
  available = data.get("available")
  
  if not (title and author and edition and available is not None):
    return jsonify({"error": "Faltan datos requeridos"}), 400
  
  book = Book(title=title,author=author,edition=edition,available=available)
  book.save()
  
  return jsonify(render_book_detail(book)), 201

@book_bp.route("/books/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_book(id):
  book = Book.get_by_id(id)
  if not book:
    return jsonify({"error": "Libro no encontrado"}), 404
  
  data = request.json
  # title,author,edition,available
  title = data.get("title")
  author = data.get("author")
  edition = data.get("edition")
  available = data.get("available")
  
  book.update(title=title,author=author,edition=edition,available=available)
  return jsonify(render_book_detail(book))

@book_bp.route("/books/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_book(id):
  book = Book.get_by_id(id)
  if not book:
    return jsonify({"error": "Libro no encontrado"}), 404
  book.delete()
  return "", 204