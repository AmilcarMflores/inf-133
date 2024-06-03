from app.database import db

class Book(db.Model):
  __tablename__ = "books"
  # title,author,edition,available
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(100), nullable=False)
  edition = db.Column(db.String(100), nullable=False)
  available = db.Column(db.Integer, nullable=False)
  
  def __init__(self,title,author,edition,available):
    self.title=title
    self.author=author
    self.edition=edition
    self.available=available
    
  def save(self):
    db.session.add(self)
    db.session.commit()
  
  @staticmethod
  def get_all():
    return Book.query.all()
  
  @staticmethod
  def get_by_id(id):
    return Book.query.get(id)
  
  # title,author,edition,available
  def update(self,title=None,author=None,edition=None,available=None):
    if title is not None:
      self.title=title
    if author is not None:
      self.author=author
    if edition is not None:
      self.edition=edition
    if available is not None:
      self.available=available
    db.session.commit()
    
  def delete(self):
    db.session.delete(self)
    db.session.commit()  
    