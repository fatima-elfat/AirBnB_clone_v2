#!/usr/bin/python3
""" ALL THE TESTS"""
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.place import Place
import unittest
from os import getenv
import pep8
import models

storage = getenv("HBNB_TYPE_STORAGE")


class Test_User_(unittest.TestCase):
    """ """

    @classmethod
    def setUp(self):
        """SetUp method"""

        self.place = Place()

    @classmethod
    def TearDown(self):
        """TearDown method."""

        del self.place

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
