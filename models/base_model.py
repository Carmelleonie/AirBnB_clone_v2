#!usr/bin/python3

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()
class BaseModel:

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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def save(self):
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        dict_t = self.__dict__.copy()
        if '__class__' in dict_t:
            dict_t['__class__'] = self.__class__.__name__
        if 'created_at' in dict_t:
            dict_t['created_at'] = self.created_at.isoformat()
        if 'updated_at' in dict_t:
            dict_t['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dict_t:
            del dict_t['_sa_instance_state']
        return dict_t


    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

