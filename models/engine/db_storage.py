#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from os import getenv


class DBStorage():


    HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
    HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
    HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
    HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')

    __engine = None
    __session = None
    
    
    def __init__(self):
    
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        
        if (getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)


    def call(self, cls=None):
        self.__session = sessionmaker(bing=self.__engine)
