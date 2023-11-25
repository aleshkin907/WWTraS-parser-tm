from sqlalchemy.orm import declarative_base
from configs.database import engine

Base = declarative_base()

def init():
    Base.metadata.create_all(bind=engine)