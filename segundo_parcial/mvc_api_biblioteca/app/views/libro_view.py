def render_book_list(books):
  # Representa una lista de libros como una lista de diccionarios
  return [
    {
      "id": book.id,
      "title": book.title,
      "author": book.author,
      "edition": book.edition,
      "availability": book.availability,
    }
    for book in books
  ]

def render_book_detail(book):
  # Representa los detalles de una libro como un diccionario
  return{
    "id": book.id,
    "title": book.title,
    "author": book.author,
    "edition": book.edition,
    "availability": book.availability,
  }