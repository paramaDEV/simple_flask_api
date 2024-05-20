from sqlalchemy import Column, Integer, String
from connection import Base

class Cinema(Base): 
    __tablename__ = 'cinema'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    city = Column(Integer)