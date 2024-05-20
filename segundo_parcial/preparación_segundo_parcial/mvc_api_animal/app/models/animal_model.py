from database import db

class Animal(db.Model):
  __tablename__ = "animals"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  specie = db.Column(db.String(100), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  
  def __init__(self,name,specie,age):
    self.name = name
    self.specie = specie
    self.age = age
    
  # Guarda un animal en la db    
  def save(self):
    db.session.add(self)
    db.session.commit()
  
  # Obtiene todos los animales de la db
  @staticmethod
  def get_all():
    return Animal.query.all()
  
  # Obtiene un animal por su id
  @staticmethod
  def get_by_id(id):
    return Animal.query.get(id)
  
  # Actualiza un animal en la db
  def update(self, name=None, specie=None, age=None):
    if name is not None:
      self.name = name
    if specie is not None:
      self.specie = specie
    if age is not None:
      self.age = age
    db.session.commit()
    
  # Elimina un animal de la db
  def delete(self):
    db.session.delete(self)
    db.session.commit()
    