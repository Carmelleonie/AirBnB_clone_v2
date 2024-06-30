#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import relationship
from os import getenv

type_of_storage = getenv('HBNB_TYPE_STORAGE')
class City(BaseModel, Base):
    """
    City: is a mapper which inherits from BaseModel ana Base
    state_id: is a column which tate id
    name: Column which contains state name
    """
    if type_of_storage == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref='cities')
    else:
        state_id = ""
        name = ""
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

