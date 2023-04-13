#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    # if models.storage_type != 'db':
    @property
    def cities(self):
        """ getter for state city instances  """
        state_cities = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                state_cities.append(city)
        return state_cities
