from sqlalchemy import Column, Integer, String
from database import Base, engine

class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True, unique=True)
    link = Column(String())
   

    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

