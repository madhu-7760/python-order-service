from sqlalchemy.orm import Session
from . import models
from pydantic import BaseModel

class OrderCreate(BaseModel):
    item: str
    quantity: int = 1

def create_order(db: Session, order_in: OrderCreate):
    db_order = models.Order(item=order_in.item, quantity=order_in.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()
