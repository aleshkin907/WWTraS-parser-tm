from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from configs.environment import get_env_variables


env = get_env_variables()

DATABASE_URL = f"{env.DATABASE_DIALECT}+psycopg2://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"

# Create db engine.
engine = create_engine(
    url=DATABASE_URL
)

# Create session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_connection():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()






