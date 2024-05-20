from database import db

class Book(db.Model):
  __tablename__ = "books"
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(100), nullable=False)
  edition = db.Column(db.String(100), nullable=False)
  available = db.Column(db.Integer, nullable=False)
  
  def __init__(self,title,author,edition,available):
    self.title = title
    self.author = author
    self.edition = edition
    self.available = available
    
  def save(self):
    db.session.add(self)
    db.session.commit()
    
  # Obtiene todos los libros de la db
  @staticmethod
  def get_all():
    return Book.query.all()
  
  # Obtiene un libro por su id
  @staticmethod
  def get_by_id(id):
    return Book.query.get(id)
  
  # Actualiza un libro por su id
  def update(self,title=None,author=None,edition=None,available=None):
    if title is not None:
      self.title = title
    if author is not None:
      self.author = author
    if edition is not None:
      self.edition = edition
    if available is not None:
      self.available = available
    # Actualizar
    db.session.commit()
    
  # Elimina un libro de la db
  def delete(self):
    db.session.delete(self)
    db.session.commit()