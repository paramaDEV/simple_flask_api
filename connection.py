from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase, Session
from flask_sqlalchemy import SQLAlchemy

 
DB_NAME = "cinema_master_db"
DB_USER = "postgres"
DB_PASS = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"
conn_str='postgresql'+'://'+DB_USER+':'+DB_PASS+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME


engine = create_engine(conn_str, echo=True)

session = Session(engine)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


