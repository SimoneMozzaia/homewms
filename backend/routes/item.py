from typing import List
from backend.schemas.item import ItemModel, ItemBase
from backend.models.item import Item
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.services.database import get_db

router = APIRouter()


@router.post("/item", response_model=ItemModel, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemBase, db: Session = Depends(get_db)):
    # Map all the variables to our table
    db_transaction = Item(**item.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction


@router.get("/item", response_model=List[ItemModel], status_code=status.HTTP_200_OK)
async def read_all_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    items = db.query(Item).offset(skip).limit(limit).all()

    return items


@router.get("/item/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Item with id {item_id} not found'
        )

    return item


@router.delete("/item/{item_id}", status_code=status.HTTP_200_OK)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Item with id {item_id} not found'
        )

    db.delete(item)
    db.commit()
