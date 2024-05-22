from connection import Base,session,db
from sqlalchemy import select, union,null, Column, Integer, String, update, ForeignKey, Row
from sqlalchemy.orm import Mapped, mapped_column, relationship
from GlobalVariable import formatSelectedData
from models.Cinema import Cinema

class Studio(Base):
    __tablename__ = 'studio'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
    capacity = mapped_column(Integer)
    status = mapped_column(Integer)
    cinema_id = mapped_column(Integer)

class StudioModel :    
    @staticmethod
    def displayStudio(studio_id = 0):
        if studio_id == 0 :
            # studios = session.query(Studio).all() #without join
            studios = session.query(Studio,Cinema).filter(Studio.cinema_id==Cinema.id).all() #with join
            result = formatSelectedData(studios)
            result = result
        else :
            studio =  session.query(Studio, Cinema).filter(Studio.id==studio_id, Cinema.id == Studio.cinema_id).order_by(Studio.id).first() # with join
            result = formatSelectedData(studio)
        return result
    
    @staticmethod
    def insertStudio(param) :
        studio = Studio(name=param['name'],capacity=param['capacity'], status=param['status'], cinema_id = param['cinema_id'])
        session.add(studio)
        session.commit()
        session.close()
        # session.rollback()

    @staticmethod
    def updateStudio(param) :
        session.execute(update(Studio).where(Studio.id == param['id']).values(capacity = param['capacity']))
        session.commit()
        session.close()


    
