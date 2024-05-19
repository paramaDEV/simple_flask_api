from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

 
DB_NAME = "cinema_master_db"
DB_USER = "postgres"
DB_PASS = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

# Start of cara lama
engine = create_engine('postgresql'+'://'+DB_USER+':'+DB_PASS+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME, echo=False)

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()
# End of cara lama

