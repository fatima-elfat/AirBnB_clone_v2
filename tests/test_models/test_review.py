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
from sqlalchemy.exc import OperationalError
import MySQLdb

storage = getenv("HBNB_TYPE_STORAGE")


class test_Review_(unittest.TestCase):
    """ UNITTEST REVIEW"""
    @classmethod
    def setUp(self):
        """SetUp method"""

        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        self.fs = FileStorage()
        self.user = User(email="Ceylin.ere@gmail.com", password="ilgaz<3")
        self.state = State(name="Istanbul")
        self.city = City(name="Istanbul", state_id=self.state.id)
        self.place = Place(
            city_id=self.city.id,
            user_id=self.user.id,
            name="Law firm")
        self.review = Review(
            place_id=self.place.id,
            user_id=self.user.id,
            text="Good consulting")
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
        del self.review
        del self.fs
        if type(models.storage) == DBStorage:
            self.dbs._DBStorage__session.close()
            del self.dbs

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.review.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Review.__doc__, "No docstring in the class")

    def test_pep8_style_check(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        s = style.check_files(['models/review.py'])
        self.assertEqual(s.total_errors, 0, "pep8 error needs fixing")

    def test_type_object(self):
        """Test type object of Review"""

        self.assertEqual(
            str(type(self.review)),
            "<class 'models.review.Review'>")
        self.assertIsInstance(self.review, Review)

    def test_Review_inheritence(self):
        """checks if inherits"""

        self.assertIsInstance(self.review, BaseModel)

    def test_db_tbname(self):
        """checks the tablename"""

        self.assertEqual(self.review.__tablename__, "reviews")

    @unittest.skipIf(storage != "db", "Testing database storage only")
    def test_Review_attributes(self):
        """ check attr"""
        place_id = getattr(self.review, "place_id")
        self.assertIsInstance(place_id, str)
        user_id = getattr(self.review, "user_id")
        self.assertIsInstance(user_id, str)
        text = getattr(self.review, "text")
        self.assertIsInstance(text, str)

    def test_init(self):
        """ checks init."""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Check for attributes."""
        rv = Review()
        self.assertEqual(str, type(rv.id))
        self.assertEqual(datetime, type(rv.created_at))
        self.assertEqual(datetime, type(rv.updated_at))
        self.assertTrue(hasattr(rv, "__tablename__"))
        self.assertTrue(hasattr(rv, "text"))
        self.assertTrue(hasattr(rv, "place_id"))
        self.assertTrue(hasattr(rv, "user_id"))

    @unittest.skipIf(
        type(models.storage) == DBStorage,
        "Testing db storage only")
    def test_save_fs(self):
        """checks save method."""
        rv = self.review.updated_at
        time.sleep(1)
        self.review.save()
        self.assertFalse(rv == self.review.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Review." + self.review.id, f.read())

    @unittest.skipIf(
        type(models.storage) == FileStorage,
        "Testing file storage only")
    def test_add_rv(self):
        """check add ."""
        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(Review(
                place_id=self.place.id,
                user_id=self.user.id))
            self.dbstorage._DBStorage__session.commit()
