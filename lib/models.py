import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, Table, PrimaryKeyConstraint, ForeignKey, Column, String, Integer)
from sqlalchemy.orm import relationship, backref,sessionmaker

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///caffeterria.db', echo=True)


rest_customers = Table(
    'rest_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer())

    customers = relationship('Customer', secondary=rest_customers, back_populates='restaurants')
    reviews = relationship('Review', backref=backref('restaurant'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'Restaurant: {self.name}'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    restaurants = relationship('Restaurant', secondary=rest_customers, back_populates='customers')
    reviews = relationship('Review', backref=backref('customer'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'Customer: {self.name}'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer())

    customer_id = Column(String(), ForeignKey('customers.id'))
    restaurant_id = Column(String(), ForeignKey('restaurants.id'))

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
                f'customer_name={self.customer_name})'+ \
                f'restaurant_name={self.restaurant_name})'+ \
                f'ratings={self.star_rating}, '

# create an engine that stores data in the local directory's school_performance.db file.
engine = create_engine('sqlite:///caffeterria.db')

# create all tables in the engine
Base.metadata.create_all(engine)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a session
session = Session()

new_restaurant = Restaurant(name='Barka Cafe', price=2000)
new_restaurant1 = Restaurant(name='Bin-Agil Cafe', price=3000)

customer1 = Customer(first_name="Jaffar",last_name="Nassor")
customer2 = Customer(first_name="Robert",last_name="Nguma")

review1 = Review(star_rating=10,customer_id="1",restaurant_id="1")


session.add(review1)
session.commit()