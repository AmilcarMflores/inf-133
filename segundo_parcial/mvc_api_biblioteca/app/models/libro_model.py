from database import db

class Book(db.Model):
  __tablename__ = "books"
  
  # Define las columnas de la tabla books
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(100), nullable=False)
  edition = db.Column(db.Integer, nullable=False)
  availability = db.Column(db.Integer, nullable=False)
  
  # Iniciamos la clase Book
  def __init__(self, title, author, edition, availability):
    self.title = title
    self.author = author
    self.edition = edition
    self.availability = availability
    
  # Guarda un animal en la bd
  def save(self):
    db.session.add(self)
    db.session.commit()
  
  # Obtiene todos los libros de la bd
  @staticmethod
  def get_all():
    return Book.query.all()
  
  # Obtiene un libro por su id
  @staticmethod
  def get_by_id(id):
    return Book.query.get(id)
  
  # Actualiza un animal en la db
  def update(self, title=None, author=None, edition=None, availability=None):
    if title is not None:
      self.title = title
    if author is not None:
      self.author = author
    if edition is not None:
      self.edition = edition
    if availability is not None:
      self.availability = availability
    db.session.commit()
    
  # Elimina un libro de la base 
  def delete(self):
    db.session.delete(self)
    db.session.commit()