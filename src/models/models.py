from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
metadata = Base.metadata

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    market_hash_name = Column(String)
    max_price = Column(int)
    min_price = Column(int)
    average_price = Column(int)
    history = Column(list)
