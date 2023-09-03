from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurant_database.db')

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    price = Column(Integer())

    reviews = relationship("Review", back_populates="restaurant")


    def __repr__(self):
        return f'Restaurant {self.name}  Price: ${self.price}.00\n'
    


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship("Review", back_populates="customer")

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}'
    

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    description = Column(String())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    star_rating = Column(Integer())

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")
    

    def __repr__(self):
        return f'{self.id}, {self.description}, {self.star_rating}'