#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import Place, place_amenity
import models


class Amenity(BaseModel, Base):
    """ Represents an Amenity for a MySQL database. """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   secondary=place_amenity
                                   )
