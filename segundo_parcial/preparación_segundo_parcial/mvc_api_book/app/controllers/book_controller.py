from flask import Blueprint, request, jsonify
from models.book_model import Book
from views.book_view import render_book_detail, render_book_list

# Crear un blueprint para el controlador de libros
book_bp = Blueprint("book", __name__)

# Ruta para obtener la lista de libros
@book_bp.route("/books", methods=["GET"])
def get_books():
  books = Book.get_all()
  return jsonify(render_book_list(books))

# Ruta para obtener un libro específico por su id
@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
  book = Book.get_by_id(id)
  if book:
    return jsonify(render_book_detail(book))
  return jsonify({"error": "Libro no encontrado"}), 404

# Ruta para crear un nuevo libro
@book_bp.route("/books", methods=["POST"])
def create_book():
  data = request.json
  
  title = data.get("title")
  author = data.get("author")
  edition = data.get("edition")
  available = data.get("available")
  
  if not title or not author or not edition or available is None:
    return jsonify({"error": "Faltan datos requeridos"}), 400
  
  book = Book(title=title,author=author,edition=edition,available=available)
  book.save()
  
  return jsonify(render_book_detail(book)), 201

# Ruta para actualizar un libro existente
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
  book = Book.get_by_id(id)
  
  if not book:
    return jsonify({"error": "Libro no encontrado"}), 404
  
  data = request.json
  title = data.get("title")
  author = data.get("author")
  edition = data.get("edition")
  available = data.get("available")
  
  book.update(title=title,author=author,edition=edition,available=available)
  
  return jsonify(render_book_detail(book))

# Ruta para eliminar un libro existente 
@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
  book = Book.get_by_id(id)
  
  if not book:
    return ({"error": "Libro no encontrado"}), 404
  
  book.delete()
  return "", 204
  

