import models
from database import Base, engine

Base.metadata.create_all(bind=engine)

for table in Base.metadata.tables:
    print(">", table)
