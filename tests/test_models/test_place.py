#!/usr/bin/python3
""" ALL THE TESTS"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest
import os
from os import getenv
import pep8
import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from datetime import datetime
import time

storage = getenv("HBNB_TYPE_STORAGE")


class Test_User_(unittest.TestCase):
    """ tests user"""

    @classmethod
    def setUp(self):
        """SetUp method"""

        self.user = User(email="Ceylin.ere@gmail.com", password="ilgaz<3")
        self.state = State(name="Istanbul")
        self.city = City(name="Istanbul", state_id=self.state.id)
        self.place = Place(
            city_id=self.city.id,
            user_id=self.user.id,
            name="Law firm")
        self.amenity = Amenity(name="Heater")
        self.review = Review(
            place_id=self.place.id,
            user_id=self.user.id,
            text="Good consulting")
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        self.fs = FileStorage()
        if type(models.storage) == DBStorage:
            self.dbs = DBStorage()
            Base.metadata.create_all(self.dbs._DBStorage__engine)
            Session = sessionmaker(bind=self.dbs._DBStorage__engine)
            self.dbs._DBStorage__session = Session()

    @classmethod
    def TearDown(self):
        """TearDown method."""

        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del self.user
        del self.state
        del self.city
        del self.place
        del self.amenity
        del self.review
        del self.fs
        if type(models.storage) == DBStorage:
            self.dbs._DBStorage__session.close()
            del self.dbs

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.place.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Place.__doc__, "No docstring in the class")

    def test_type_object(self):
        """Test type object of Place"""

        self.assertEqual(
            str(type(self.place)),
            "<class 'models.place.Place'>")
        self.assertIsInstance(self.place, Place)

    def test_pep8_style_check(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        s = style.check_files(['models/place.py'])
        self.assertEqual(s.total_errors, 0, "pep8 error needs fixing")

    def test_type_object(self):
        """Test type object of place"""

        self.assertEqual(
            str(type(self.place)),
            "<class 'models.place.Place'>")
        self.assertIsInstance(self.place, Place)

    def test_place_inheritence(self):
        """checks if inherits"""

        self.assertIsInstance(self.place, BaseModel)

    def test_db_tbname(self):
        """checks the tablename"""

        self.assertEqual(self.place.__tablename__, "places")

    @unittest.skipIf(storage != "db", "Testing database storage only")
    def test_place_amenity_dbattrb(self):
        self.assertTrue("amenities" in self.new_place.__dir__())
        self.assertTrue("reviews" in self.new_place.__dir__())

    def test_attributes(self):
        """Check for attributes."""
        pl = Place()
        self.assertEqual(str, type(pl.id))
        self.assertEqual(datetime, type(pl.created_at))
        self.assertEqual(datetime, type(pl.updated_at))
        self.assertTrue(hasattr(pl, "__tablename__"))
        self.assertTrue(hasattr(pl, "city_id"))
        self.assertTrue(hasattr(pl, "name"))
        self.assertTrue(hasattr(pl, "description"))
        self.assertTrue(hasattr(pl, "number_rooms"))
        self.assertTrue(hasattr(pl, "number_bathrooms"))
        self.assertTrue(hasattr(pl, "max_guest"))
        self.assertTrue(hasattr(pl, "price_by_night"))
        self.assertTrue(hasattr(pl, "latitude"))
        self.assertTrue(hasattr(pl, "longitude"))
        self.assertTrue(hasattr(pl, "amenity_ids"))

    @unittest.skipIf(
        type(models.storage) == DBStorage,
        "Testing db storage only")
    def test_save_fs(self):
        """checks save method."""
        pl = self.place.updated_at
        time.sleep(1)
        self.place.save()
        self.assertFalse(pl == self.place.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Place." + self.place.id, f.read())
