#!/usr/bin/python3
"""New class for SQLAlchemy"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity



class DBStorage:
    """Create tables in the environment"""

    __engine = None
    __session = None

    def __init__(self):
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_password = getenv("HBNB_MYSQL_PWD")
        mysql_db = getenv("HBNB_MYSQL_DB")
        mysql_host = getenv("HBNB_MYSQL_HOST")
        environment = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(mysql_user, mysql_password, mysql_host, mysql_db),
                                      pool_pre_ping=True)

        if environment == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None) -> dict:
        """Return a dictionary of objects"""
        objects = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                query = self.__session.query(cls)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj) -> None:
        """Add a new object to the session"""
        self.__session.add(obj)

    def save(self) -> None:
        """Save changes to the database"""
        self.__session.commit()

    def delete(self, obj=None) -> None:
        """Delete an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self) -> None:
        """Configure the session and create tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self) -> None:
        """Close the session"""
        self.__session.close()
