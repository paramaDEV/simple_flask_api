from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import mapped_column, relationship
from connection import Base, session
from GlobalVariable import *

class Cinema(Base): 
    __tablename__ = 'cinema'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
    city = mapped_column(Integer)

class CinemaModel : 
    @staticmethod 
    def displayCinema(cinema_id):
        result = session.scalars(select(Cinema)).all()
        result = formatSelectedData(result)
        print(result)
        return result