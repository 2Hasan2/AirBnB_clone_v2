#!/usr/bin/python3
"""Defines the City class."""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Defines the City class."""
    __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="cities")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance."""
        super().__init__(*args, **kwargs)
