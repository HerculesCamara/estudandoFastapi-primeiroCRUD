from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Aqui estou pegando a URL do db
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Funcao para ter uma sessao do db em cada request
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()