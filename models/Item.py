from sqlalchemy import  Integer, Column
from models.base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    market_hash = Column(Integer)

    # Other fields




