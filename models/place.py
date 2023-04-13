#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, Integer, String, ForeignKey,
                        Float, Table, ForeignKey)
from sqlalchemy.orm import relationship
import models
import os


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey(
                    "cities.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(String(60), ForeignKey(
                    "users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")

        reviews = relationship("Review",
                               cascade="all, delete, delete-orphan",
                               backref="place")

    else:
        @property
        def amenities(self):
            self.amenity_ids = models.storage.all(Amenity)
            amenity_list = [amenity for amenity in
                            models.storage.all(Amenity).values()
                            if amenity.id in amenity_ids]
            return amenity_list

        @amenities.setter
        def amenities(self, amenity_obj):
            if type(amenity_obj) == type(self):
                self.amenity_ids.append(amenity_obj.id)

        @property
        def reviews(self):
            """ getter for place reviews instances  """
            place_reviews = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    place_reviews.append(review)
            return place_reviews
