#!/usr/bin/python3
""" ALL THE TESTS"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel
import unittest
from os import getenv
import pep8
import models
from models.engine.db_storage import DBStorage


class test_User_(unittest.TestCase):
    """ UNITTEST USER"""
    @classmethod
    def setUp(self):
        """SetUp method"""

        self.user = User()
        self.user.email = "ilgaz@gmail.com"
        self.user.password = "yargi1@"
        self.user.first_name = "ilgaz"
        self.user.last_name = "kaya"

    @classmethod
    def TearDown(self):
        """TearDown method."""

        del self.user

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.user.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(User.__doc__, "No docstring in the class")

    def test_pep8_style_check(self):
        """Test pep8"""

        style = pep8.StyleGuide(quiet=True)
        s = style.check_files(['models/user.py'])
        self.assertEqual(s.total_errors, 0, "pep8 error needs fixing")

    def test_type_object(self):
        """Test type object of User"""

        self.assertEqual(
            str(type(self.user)),
            "<class 'models.user.User'>")
        self.assertIsInstance(self.user, User)

    def test_User_inheritence(self):
        """checks if inherits"""

        self.assertIsInstance(self.user, BaseModel)

    def test_db_tbname(self):
        """checks the tablename"""

        self.assertEqual(self.user.__tablename__, "users")

    @unittest.skipIf(
        type(models.storage) == DBStorage,
        "Testing database storage only")
    def test_attr(self):
        """ """
        email = getattr(self.user, "email")
        self.assertIsInstance(email, str)
        first_name = getattr(self.user, "first_name")
        self.assertIsInstance(first_name, str)
        last_name = getattr(self.user, "last_name")
        self.assertIsInstance(last_name, str)
        password = getattr(self.user, "password")
        self.assertIsInstance(password, str)
