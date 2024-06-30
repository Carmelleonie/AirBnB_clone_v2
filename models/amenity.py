#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

type_of_storage = getenv('HBNB_TYPE_STORAGE')

class Amenity(BaseModel, Base):

    if type_of_storage == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")
    else:
        """name: string - empty string"""
        name = ""
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

