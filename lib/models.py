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
    customers = relationship("Customer", secondary="reviews", back_populates="restaurants")

    # get all reviews for this restaurant
    @property
    def restaurant_reviews(self):
        return self.reviews
    
    # get the customers who reviewed this restaurant
    @property
    def restaurant_customers(self):
        return [review.customer for review in self.reviews]


    def __repr__(self):
        return f'Restaurant {self.name}  Price: ${self.price}.00\n'
    


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers")

    #customer reviews
    @property
    def customer_reviews(self):
        return self.reviews
    
    #customer restaurants
    @property
    def customer_restaurants(self):
        return self.restaurants

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

    #all reviews
    def full_reviews(self):
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars" for review in self.reviews]
    
    #instances
    @property
    def review_restaurant(self):
        return self.restaurant

    

    def __repr__(self):
        return f'{self.id}, {self.description}, {self.star_rating}'