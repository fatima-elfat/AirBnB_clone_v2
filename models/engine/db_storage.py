#!/usr/bin/python3
""" A new engine DBStorage with SqlAlchemy"""
from sqlalchemy import MetaData
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    Database storage engine
    """

    __engine = None
    __session = None

    def __init__(self):
        """DBstorage instances"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db_name),
            pool_pre_ping=True,
        )
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        storage_dict = {}
        if cls is True:
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                storage_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for all_class in classes:
                query = self.__session.query(all_class).all()
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    storage_dict[key] = obj

        return storage_dict

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        self.__session.delete(obj)

    def reload(self):
        """reload all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session()

    def close(self):
        """close the current session"""
        self.__session.close()
