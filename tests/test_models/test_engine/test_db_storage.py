#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session

DBStorage = db_storage.DBStorage
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(self):
        """Set up for the doc tests"""
        if type(models.storage) == DBStorage:
            self.storage = DBStorage()
            Base.metadata.create_all(self.storage._DBStorage__engine)
            sesh = sessionmaker(bind=self.storage._DBStorage__engine)
            self.storage._DBStorage__session = sesh()
            self.user = User(email="Ceylin.ere@gmail.com", password="ilgaz<3")
            self.storage._DBStorage__session.add(self.user)
            self.state = State(name="Istanbul")
            self.storage._DBStorage__session.add(self.state)
            self.city = City(name="Istanbul", state_id=self.state.id)
            self.storage._DBStorage__session.add(self.city)
            self.place = Place(
                city_id=self.city.id,
                user_id=self.user.id,
                name="Law firm")
            self.storage._DBStorage__session.add(self.place)
            self.amenity = Amenity(name="Heater")
            self.storage._DBStorage__session.add(self.amenity)
            self.review = Review(
                place_id=self.place.id,
                user_id=self.user.id,
                text="Good consulting")
            self.storage._DBStorage__session.add(self.review)
            self.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(self):
        """TearDown method."""

        if type(models.storage) == DBStorage:
            self.storage._DBStorage__session.delete(self.user)
            del self.user
            self.storage._DBStorage__session.delete(self.state)
            del self.state
            self.storage._DBStorage__session.delete(self.review)
            del self.review
            self.storage._DBStorage__session.delete(self.place)
            del self.place
            self.storage._DBStorage__session.delete(self.city)
            del self.city
            self.storage._DBStorage__session.delete(self.amenity)
            del self.amenity
            self.storage._DBStorage__session.commit()
            self.storage._DBStorage__session.close()
            del self.storage

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    @unittest.skipIf(
        type(models.storage) == FileStorage,
        "Testing file storage only")
    def test_strg_attr(self):
        """Check the bdstorage attributes."""
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))

    @unittest.skipIf(
        type(models.storage) == FileStorage,
        "Testing file storage only")
    def test_init(self):
        """Test init."""
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(isinstance(self.storage, DBStorage))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""
