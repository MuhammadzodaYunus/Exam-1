from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv
from sqlalchemy.orm import DeclarativeBase, sessionmaker


load_dotenv()

DATABASE_URL=getenv("DATABASE_URL")

engine = create_engine(url=DATABASE_URL, echo=True)

SessionMaker = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionMaker()
    try:
        yield db
    finally:
        db.close()