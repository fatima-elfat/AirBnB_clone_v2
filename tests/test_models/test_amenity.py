#!/usr/bin/python3
""" ALL THE TESTS"""
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
from os import getenv
import pep8
import models

storage = getenv("HBNB_TYPE_STORAGE")


class test_Amenity_(unittest.TestCase):
    """ UNITTEST AMENIYTY"""
    @classmethod
    def setUp(self):
        """SetUp method"""

        self.amenity = Amenity()
        self.amenity.name = "GYM"

    @classmethod
    def TearDown(self):
        """TearDown method."""

        del self.amenity

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.amenity.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Amenity.__doc__, "No docstring in the class")

    def test_pep8_style_check(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        s = style.check_files(['models/amenity.py'])
        self.assertEqual(s.total_errors, 0, "pep8 error needs fixing")

    def test_type_object(self):
        """Test type object of Amenity"""

        self.assertEqual(
            str(type(self.amenity)),
            "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(self.amenity, Amenity)

    def test_Amenity_inheritence(self):
        """checks if inherits"""

        self.assertIsInstance(self.amenity, BaseModel)

    def test_db_tbname(self):
        """checks the tablename"""

        self.assertEqual(self.amenity.__tablename__, "amenities")

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_attr(self):
        """ checks attr"""
        name = getattr(self.amenity, "name")
        self.assertIsInstance(name, str)
