#!/usr/bin/python3
"""Defines the Review class."""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey



class Review(BaseModel, Base):
    """Defines the Review class."""
    __tablename__ = "reviews"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance."""
        super().__init__(*args, **kwargs)
