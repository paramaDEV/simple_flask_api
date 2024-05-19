from connection import Base,session
from sqlalchemy import *


class Studio(Base):
    __tablename__ = 'studio'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    capacity = Column(Integer)
    status = Column(Integer)
    cinema_id = Column(Integer)

class StudioModel :    
    def displayStudio():
        studios = session.query(Studio).order_by(Studio.id).all()
        result  = [u.__dict__ for u in studios]
        for u in result :  u.pop('_sa_instance_state')
        return result