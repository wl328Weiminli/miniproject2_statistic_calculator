from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, FLOAT
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from pprint import pprint

engine = create_engine('sqlite:////web/Sqlite-Data/lwm.db')
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'Customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    town = Column(String(250), nullable=False)


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cost_price = Column(FLOAT, nullable=False)
    selling_price = Column(FLOAT, nullable=False)
    quantity = Column(FLOAT, nullable=False)


Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c1, c2])
session.commit()
