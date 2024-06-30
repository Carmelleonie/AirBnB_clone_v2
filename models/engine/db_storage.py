#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from os import getenv


class DBStorage():


    HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
    HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
    HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
    HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')

    __engine = None
    __session = None
    
    type_of_class = {'Amenity': Amenity,
                     'City': City,
                     'Place': Place,
                     'Review': Review,
                     'State': State,
                     'User': User
                    }
    
    
    def __init__(self):
    
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        
        if (getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)
            self.__session = sessionmaker(bing=self.__engine)


    def call(self, cls=None):
        _dict = {}
        if cls != None:
            query = self.__session.query(cls).all()
            for row in query:
                key = "{}.{}".format(cls.__name__, row.id)
                _dict[key] = row
        else:
            for k in type_of_class.keys():
                if cls is type_of_class[k]:
                    query = self.__session.query(type_of_class[k]).all()
                    for row in query:
                        key = "{}.{}".format(cls.__name__, row.id)
                        _dict[key] = row
        return _dict


    def new(self, obj):
        """add the object to the current database session"""
        self.__session(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

