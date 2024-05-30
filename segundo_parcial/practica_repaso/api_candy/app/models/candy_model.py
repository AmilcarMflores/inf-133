from database import db

class Candy(db.Model):
  __tablename__ = "candies"
  # marca, peso, sabor, origen
  id = db.Column(db.Integer, primary_key=True)
  brand = db.Column(db.String(100), nullable=False)
  weight = db.Column(db.Float, nullable=False)
  flavor = db.Column(db.String(100), nullable=False)
  origin = db.Column(db.String(100), nullable=False)
  
  def __init__(self,brand,weight,flavor,origin):
    self.brand=brand
    self.weight=weight
    self.flavor=flavor
    self.origin=origin
    
  def save(self):
    db.session.add(self)
    db.session.commit()
    
  @staticmethod
  def get_all():
    return Candy.query.all()
  
  @staticmethod
  def get_by_id(id):
    return Candy.query.get(id)
  
  def update(self,brand=None,weight=None,flavor=None,origin=None):
    if brand is not None:
      self.brand=brand
    if weight is not None:
      self.weight=weight
    if flavor is not None:
      self.flavor=flavor
    if origin is not None:
      self.origin=origin
    db.session.commit()
    
  def delete(self):
    db.session.delete(self)
    db.session.commit()    
    