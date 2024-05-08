from flask import Blueprint, request, jsonify
from models.libro_model import Book
from views.libro_view import render_book_list, render_book_detail

# Crear un blueprint para el controlador de libros
book_bp = Blueprint("book", __name__)

# Ruta para obtener la lista de libros
@book_bp.route("/books", methods=["GET"])
def get_books():
  books = Book.get_all()
  return jsonify(render_book_list(books))

# Ruta para obtener un animal específico por su id
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
  availability = data.get("availability")
  
  # Validación simple de datos de entrada
  if not title or not author or edition is None or availability is None:
    return jsonify({"error": "Faltan datos requeridos"}), 400
  
  # Crear un nuevo libro y guardarlo en db
  book = Book(title=title, author=author, edition=edition, availability=availability)
  book.save()
  
  return jsonify(render_book_detail(book)), 201

# Ruta para actualizar un animal existente
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
  book = Book.get_by_id(id)
  
  if not book:
    return jsonify({"error": "Libro no encontrado"}), 404
  
  data = request.json
  title = data.get("title")
  author = data.get("author")
  edition = data.get("edition")
  availability = data.get("availability")
  
  # Actualizar los datos del libro
  book.update(title=title, author=author, edition=edition, availability=availability)
  
  return jsonify(render_book_detail(book))

# Ruta para eliminar un libro existente
@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
  book = Book.get_by_id(id)
  
  if not book:
    return jsonify({"error": "Libro no encontrado"}), 404
  
  # Eliminar el libro de la db
  book.delete()
  
  # Respuesta vacía con código de estado 204 (sin contenido)
  return "", 204
