#!/usr/bin/python3
""" ALL THE TESTS"""
from os import getenv
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


storage = getenv("HBNB_TYPE_STORAGE")


class test_Amenity(unittest.TestCase):
    """ UNITTEST AMENIYTY"""
    @classmethod
    def setUp(self):
        """SetUp method"""

        self.amenity = Amenity()
        self.new_amenity.name = "GYM"

    @classmethod
    def TearDown(self):
        """TearDown method."""

        del self.amenity

    def test_type_object(self):
        """Test type object of Amenity"""

        self.assertEqual(
            str(type(self.amenity)),
            "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(self.amenity, Amenity)

    def test_Amenity_inheritence(self):
        """checks if inherits"""

        self.assertIsInstance(self.new_amenity, BaseModel)

    def test_db_tbname(self):
        """checks the tablename"""

        self.assertEqual(self.new_amenity.__tablename__, "amenities")

    def test_attr(self):
        """ checks the attributes"""

        self.assertTrue("name" in self.new_amenity.__dir__())
        if storage == 'db':
            name_value = getattr(self.new_amenity, "name")
            self.assertIsInstance(name_value, str)
