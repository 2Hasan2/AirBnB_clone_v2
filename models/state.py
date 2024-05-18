#!/usr/bin/python3
"""Defines the State class."""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Defines the State class."""
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """returns a list of City instances with state_id equal to the current State.id"""
            cityList = []
            for key, value in models.storage.all(City).items():
                if value.state_id == self.id:
                    cityList.append(value)
            return cityList
