from pydantic import BaseModel
import datetime as dt


class ItemBase(BaseModel):
    name: str
    description: str
    category: str
    barcode: str
    weight: float
    dangerous: bool
    fragile: bool
    update_user: str
    creation_date: dt.datetime
    update_date: dt.datetime


class ItemModel(ItemBase):
    id: int

    class Config:
        orm_mode = True


