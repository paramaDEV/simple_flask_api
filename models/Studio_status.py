from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import mapped_column, relationship
from connection import Base, session
from GlobalVariable import *

class Studio_status(Base): 
    __tablename__ = 'studio_status'
    id = mapped_column(Integer, primary_key=True)
    text = mapped_column(String(100))
