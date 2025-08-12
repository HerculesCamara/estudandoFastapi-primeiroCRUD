from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
  db_item = models.Item(name=item.name, description=item.description, imageURL=item.imageURL)
  db.add(db_item)
  db.commit()
  db.refresh(db_item)
  return db_item

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
      raise HTTPExeption(status_code=404, detail="Item nao encontrado")
    return db_item

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
  db_item = db.query(models.Item)
  if db_item is None:
    raise HTTPException(status_code=404, detail="Item nao encontrado")
  db_item.name = item.name
  db_item.description = item.description
  db_item.imageURL = item.imageURL
  db.commit()
  db.refresh(db_item)
  return db_item

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
  db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
  if db_item is None:
    raise HTTPException(status_code=404, detail="Item nao encontrado")
  db.delete(db_item)
  db.commit()
  return db_item