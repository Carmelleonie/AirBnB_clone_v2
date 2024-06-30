#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import *
from os import getenv

type_of_storage = getenv('HBNB_TYPE_STORAGE')

if type_of_storage == "db":
    place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), nullable=False)
        Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False)
    )
class Place(BaseModel, Base):

    """
    Place inherits from BaseModel and Base (respect the order)
    Add or replace in the class Place:
        class attribute __tablename__
            represents the table name, places
        class attribute city_id
            represents a column containing a string (60 characters)
            can’t be null
            is a foreign key to cities.id
        class attribute user_id
            represents a column containing a string (60 characters)
            can’t be null
            is a foreign key to users.id
        class attribute name
            represents a column containing a string (128 characters)
            can’t be null
        class attribute description
            represents a column containing a string (1024 characters)
            can be null
        class attribute number_rooms
            represents a column containing an integer
            can’t be null
            default value: 0
        class attribute number_bathrooms
            represents a column containing an integer
            can’t be null
            default value: 0
        class attribute max_guest
            represents a column containing an integer
            can’t be null
            default value: 0
        class attribute price_by_night
            represents a column containing an integer
            can’t be null
            default value: 0
        class attribute latitude
            represents a column containing a float
            can be null
        class attribute longitude
            represents a column containing a float
            can be null

    """
    if type_of_storage == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeognKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer(), nullable=False, default=0)
        number_bathrooms = Column(Integer(), nullable=False, default=0)
        max_guest = Column(Integer(), nullable=False, default=0)
        price_by_night = Column(Integer(), nullable=False, default=0)
        latitude = Column(Float(), nullable=False, default=0.0)
        longitude = Column(Float(), nullable=False, default=0.0)
        amenities = relationship("Amenity", secondary="place_amenity", back_populates="places", viewonly=False)
        reviews = relationship("Review", backref="places")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        def __init__(self, *args, **kwargs):
        """initializes Place"""
            super().__init__(*args, **kwargs)

        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

