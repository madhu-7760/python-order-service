from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud, database
from .crud import OrderCreate

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Order Service")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/orders", response_model=dict)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    created = crud.create_order(db, order)
    return {"id": created.id, "item": created.item, "quantity": created.quantity, "created_at": created.created_at.isoformat()}

@app.get("/orders/{order_id}", response_model=dict)
def get_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"id": order.id, "item": order.item, "quantity": order.quantity, "created_at": order.created_at.isoformat()}

@app.get("/health")
def health():
    return {"status": "ok"}


