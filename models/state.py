#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

_storage = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """This class  is inherited from BaseModel and it is an empty string"""




    if _storage == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='states')
    else:
        name = ""
        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
        
            cities_list = []
            for key, value in models.storage.all(City).items():
                if value.state_id == self.id:
                    cities_list.append(value)
            return cities_list

