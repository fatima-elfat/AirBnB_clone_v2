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


class test_Place(test_basemodel):
    """ TESTS Place"""

    def __init__(self, *args, **kwargs):
        """ INIT VALUE OF CLASS"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ CHECK IF TYPE OF CITY ID"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ CHECK IF TYPE OF USER ID"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ CHECK IF TYPE OF NAME"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ CHECK IF TYPE OF DESCR"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ CHECK IF TYPE OF ..."""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ CHECK IF TYPE OF ..."""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ CHECK IF TYPE OF ..."""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ CHECK IF TYPE OF ..."""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ CHECK IF TYPE OF ..."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ CHECK IF TYPE OF ..."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_place_ids(self):
        """ CHECK IF TYPE OF ..."""
        new = self.value()
        self.assertEqual(type(new.place_ids), list)


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
