from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker

 
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/lab9"
 

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)

print("Таблицы успешно созданы.")
