#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlachemy import String, ForeignKey

Base = declarative_base()
class City(BaseModel, Base):
    """
    City: is a mapper which inherits from BaseModel ana Base
    state_id: is a column which tate id
    name: Column which contains state name
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
