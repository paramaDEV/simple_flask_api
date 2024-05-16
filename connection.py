from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

 
DB_NAME = "cinema"
DB_USER = "postgres"
DB_PASS = "admin"
DB_HOST = "localhost"
DB_PORT = "5433"

engine = create_engine('postgresql'+'://'+DB_USER+':'+DB_PASS+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME, echo=False)

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()