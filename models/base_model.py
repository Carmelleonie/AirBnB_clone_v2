#!usr/bin/python3

import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()
class BaseModel:


    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs):
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        dict_t = self.__dict__.copy()
        dict_t['__class__'] = self.__class__.__name__
        dict_t['created_at'] = self.created_at.isoformat()
        dict_t['update_at'] = self.updated_at.isoformat()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
