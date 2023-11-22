#!/usr/bin/python3
""" ALL THE TESTS"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.base_model import BaseModel
import unittest
from os import getenv
import pep8
import models
from models.engine.db_storage import DBStorage


class test_State_(unittest.TestCase):
    """ UNITTEST STATE"""
    @classmethod
    def setUp(self):
        """SetUp method"""

        self.state = State()
        self.state.name = "EZ4"

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

    @unittest.skipIf(
        type(models.storage) == DBStorage,
        "Testing database storage only")
    def test_attr(self):
        """ checks attr"""
        new = getattr(self.state, "name")
        self.assertIsInstance(new, str)
