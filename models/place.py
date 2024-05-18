#!/usr/bin/python3
"""Defines the Place class."""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """Defines the Place class."""
    __tablename__ = "places"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity")
    else:
        name = ""
        city_id = ""
        user_id = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        @property
        def reviews(self):
            """returns a list of Review instances with place_id equal to the current Place.id"""
            reviewList = []
            for key, value in models.storage.all(Review).items():
                if value.place_id == self.id:
                    reviewList.append(value)
            return reviewList

        @property
        def amenities(self):
            """returns a list of Amenity instances with place_id equal to the current Place.id"""
            amenityList = []
            for key, value in models.storage.all(Amenity).items():
                if value.place_id == self.id:
                    amenityList.append(value)
            return amenityList
