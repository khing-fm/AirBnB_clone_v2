#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os


class DBStorage:
    """This class manages db storage of hbnb models using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        temp_dict = {}
        if cls is None:
            classes = [State, City, User, Place, Amenity, Review]
            for clss in classes:
                results = self.__session.query(clss).all()
                for result in results:
                    temp_dict[clss.__name__ + '.' + result.id] = result
        else:
            results = self.__session.query(cls).all()
            for result in results:
                temp_dict[cls.__name__ + '.' + result.id] = result
        return temp_dict

    def new(self, obj):
        """ add a new element in the table """
        self.__session.add(obj)

    def save(self):
        """ save changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete an element in the table """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload configuration """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ closes sqlalchemy session """
        self.__session.close()
