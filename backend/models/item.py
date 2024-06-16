from backend.services.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.sql import func


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    category = Column(String, index=True)
    barcode = Column(String, index=True)
    weight = Column(Float)
    dangerous = Column(Boolean)
    fragile = Column(Boolean)
    update_user = Column(String) #TODO In the future link the "USER" model
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    update_date = Column(DateTime(timezone=True), onupdate=func.now())



