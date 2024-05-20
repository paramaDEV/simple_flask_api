from connection import Base,session,db
from sqlalchemy import select, null, Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from GlobalVariable import formatSelectedData
from models.Cinema import Cinema

class Studio(Base):
    __tablename__ = 'studio'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    capacity = Column(Integer)
    status = Column(Integer)
    cinema_id = Column(Integer)

class StudioModel :    
    @staticmethod
    def displayStudio(studio_id = 0):
        if studio_id == 0 :
            studios = session.query(Studio).order_by(Studio.id).all()  
            result = formatSelectedData(studios)
        else :
            studio =  session.query(Studio).filter(Studio.id==studio_id).order_by(Studio.id).first()
            result = formatSelectedData(studio)
        return result
    
    @staticmethod
    def insertStudio(param) :
        print(param)
        print('<================================>')
        studio = Studio(name=param['name'],capacity=param['capacity'], status=param['status'], cinema_id = param['cinema_id'])
        session.add(studio)
        session.commit()
        session.close()
    
