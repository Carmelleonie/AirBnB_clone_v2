#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

type_of_db = getenv('HBNB_TYPE_STORAGE')
if type_of_db == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
