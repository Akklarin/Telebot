from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:{__MyPASSWORD__}@localhost:5432/BHhw')
TestSession = sessionmaker(bind=engine)

Base = declarative_base()


class Employees(Base):
    __tablename__ = 'employees'
    name = Column(String, primary_key=True)
    age = Column(Integer)
    place_of_work = Column(String)


def info_write(n, a, wp):
    new_employee = Employees(name=n, age=a, place_of_work=wp)
    session.add(new_employee)
    session.commit()


Base.metadata.create_all(engine)
session = TestSession()
