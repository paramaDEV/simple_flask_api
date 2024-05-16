from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql://postgres:admin@localhost:5433/cinema', echo=False)

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

student1 = Student(name='Fany23')
student2 = Student(name='Dodywqe')
student3 = Student(name='Anjiqwe')

# Base.metadata.create_all(engine)
# session.add_all([student2,student3])
# session.commit()
# session.close()

students = session.query(Student).order_by(Student.name).filter(Student.name=='Fany').first()
# students = session.query(Student).order_by(Student.name).first()
# for s in students :
#     # s.name = 'Fany'
#     print(s.name)
session.delete(students)
session.commit()

