#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv

type_of_storage = getenv('HBNB_TYPE_STORAGE')

class Review(BaseModel, Base):


    if type_of_storage == "db":
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    else:
        """
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
        """
        place_id = ""
        user_id = ""
        text = ""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

