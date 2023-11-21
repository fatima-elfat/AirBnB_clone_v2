#!/usr/bin/python3
""" ALL THE TESTS"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel
import unittest
from os import getenv
import pep8
import models

storage = getenv("HBNB_TYPE_STORAGE")


class test_City(test_basemodel):
    """ TESTS CITY"""

    def __init__(self, *args, **kwargs):
        """ INIT VALUE OF CLASS"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ CHECK IF STATE ID"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ CHECK IF TYPE OF NAME IS STR"""
        new = self.value()
        self.assertEqual(type(new.name), str)


class test_City_(unittest.TestCase):
    """ UNITTEST CITY"""
    @classmethod
    def setUp(self):
        """SetUp method"""

        self.city = City()
        self.city.state_id = "AZ1"
        self.city.name = "EL JADIDA"

    @classmethod
    def TearDown(self):
        """TearDown method."""

        del self.city

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.city.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(City.__doc__, "No docstring in the class")

    def test_pep8_style_check(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        s = style.check_files(['models/city.py'])
        self.assertEqual(s.total_errors, 0, "pep8 error needs fixing")

    def test_type_object(self):
        """Test type object of city"""

        self.assertEqual(
            str(type(self.city)),
            "<class 'models.city.City'>")
        self.assertIsInstance(self.city, City)

    def test_city_inheritence(self):
        """checks if inherits"""

        self.assertIsInstance(self.city, BaseModel)

    def test_db_tbname(self):
        """checks the tablename"""

        self.assertEqual(self.city.__tablename__, "cities")

    def test_attr(self):
        """ checks the attributes"""

        self.assertTrue("name" in self.city.__dir__())
        if storage == 'db':
            name_value = getattr(self.city, "name")
            state_id = getattr(self.city, "state_id")
            self.assertIsInstance(name_value, str)
            self.assertEqual(state_id, str)
