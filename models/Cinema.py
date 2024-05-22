from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, relationship
from connection import Base

class Cinema(Base): 
    __tablename__ = 'cinema'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
    city = mapped_column(Integer)