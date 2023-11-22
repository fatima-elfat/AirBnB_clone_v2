#!/usr/bin/python3
""" ALL THE TESTS"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.base_model import BaseModel
import unittest
from os import getenv
import pep8
import models

storage = getenv("HBNB_TYPE_STORAGE")


class test_Review_(unittest.TestCase):
    """ UNITTEST REVIEW"""
    @classmethod
    def setUp(self):
        """SetUp method"""

        self.review = Review()

    @classmethod
    def TearDown(self):
        """TearDown method."""

        del self.review

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
