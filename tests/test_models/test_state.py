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


class test_State_(unittest.TestCase):
    """ UNITTEST STATE"""
    @classmethod
    def setUp(self):
        """SetUp method"""

        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        self.fs = FileStorage()
        self.state = State(name="Istanbul")
        self.city = City(name="Istanbul", state_id=self.state.id)
        if type(models.storage) == DBStorage:
            self.dbs = DBStorage()
            Base.metadata.create_all(self.dbs._DBStorage__engine)
            Session = sessionmaker(bind=self.dbs._DBStorage__engine)
            self.dbs._DBStorage__session = Session()

    @classmethod
    def TearDown(self):
        """TearDown method."""

        del self.state

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.state.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(State.__doc__, "No docstring in the class")

    def test_pep8_style_check(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        s = style.check_files(['models/state.py'])
        self.assertEqual(s.total_errors, 0, "pep8 error needs fixing")

    def test_type_object(self):
        """Test type object of State"""

        self.assertEqual(
            str(type(self.state)),
            "<class 'models.state.State'>")
        self.assertIsInstance(self.state, State)

    def test_State_inheritence(self):
        """checks if inherits"""

        self.assertIsInstance(self.state, BaseModel)

    def test_db_tbname(self):
        """checks the tablename"""

        self.assertEqual(self.state.__tablename__, "states")

    def test_init(self):
        """ checks init."""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Check for attributes."""
        st = State()
        self.assertEqual(str, type(st.id))
        self.assertEqual(datetime, type(st.created_at))
        self.assertEqual(datetime, type(st.updated_at))
        self.assertTrue(hasattr(st, "__tablename__"))
        self.assertTrue(hasattr(st, "name"))

    @unittest.skipIf(
        type(models.storage) == DBStorage,
        "Testing db storage only")
    def test_save_fs(self):
        """checks save method."""
        st = self.state.updated_at
        time.sleep(1)
        self.state.save()
        self.assertFalse(st == self.state.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("State." + self.state.id, f.read())

    @unittest.skipIf(
        type(models.storage) == FileStorage,
        "Testing file storage only")
    def test_add_st(self):
        """check add ."""
        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(State())
            self.dbstorage._DBStorage__session.commit()
