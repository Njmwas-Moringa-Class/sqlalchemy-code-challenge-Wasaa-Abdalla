import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, Table, PrimaryKeyConstraint, ForeignKey, Column, String, Integer)
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)


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

