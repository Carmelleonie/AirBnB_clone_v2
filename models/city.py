#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=Fasle)
    