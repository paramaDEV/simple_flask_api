from connection import Base,session
from sqlalchemy import *

class Studio(Base):
    __tablename__ = 'studio'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    capacity = Column(Integer)
    status = Column(Integer)

class StudioModel :    
    def displayStudio():
        return 'gas'