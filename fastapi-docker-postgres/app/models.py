from sqlalchemy import Column, Integer, String
from .database import Base

# O 'Base' é o cara que vai permitir traduzir a classe em python para criação de tabelas no bd
class Item(Base):
  __tablename__ = "items"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String, index=True, nullable=True)
  imageURL = Column(String, index=True, nullable=True)

  def __init__(self, name: str, description: str = None, imageURL: str = None):
    self.nome = name
    self.description = description
    self.imageURL = imageURL