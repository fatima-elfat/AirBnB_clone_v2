#!/usr/bin/python3
""" ALL THE TESTS"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import models
import pycodestyle
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE")


class test_basemodel(unittest.TestCase):
    """ TESTS BASE MODEL"""

    def __init__(self, *args, **kwargs):
        """ INIT VALUE OF CLASS"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """SetUp method"""

        pass

    def tearDown(self):
        """TearDown method."""

        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """TEST THE VALUE"""

        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """TEST KWARGS"""

        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_docstring(self):
        """Test docstring for the module and the class"""

        self.assertIsNotNone(
            models.base_model.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(BaseModel.__doc__, "No docstring in the class")

    def test_pycodestyle(self):
        """ tests the  pep8"""
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        p = pycostyle.check_files(['models/base_model.py'])
        self.assertEqual(
                p.total_errors,
                0,
                "Found code style errors (and warnings).")

    def test_kwargs_int(self):
        """TEST KWARGS"""

        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """TEST str"""

        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """TEST TO DICT"""

        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """TEST KWARGS NONE"""

        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        '''TEST KWARGS ONE VALUE'''

        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """TEST id"""

        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """TEST created_at"""

        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_update(self):
        """ test update at"""

        new = self.value()
        o = new.updated_at
        new.save()
        self.assertNotEqual(new.updated_at, o)

    def test_mod_to_dict(self):
        """Test dictionary representation in BaseModel"""

        new = self.value()
        n = new.to_dict()
        self.assertIsInstance(n, dict)

    def test_type_object(self):
        """Test type object of BaseModel"""

        new = self.value()
        self.assertEqual(
            str(type(new)),
            "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(new, BaseModel)

    def test_str_representation(self):
        """Test str representation of BaseModel"""

        new = self.value()
        str_rep = "[{:s}] ({:s}) {:s}".format(
            new.__class__.__name__,
            new.id,
            str(new.__dict__)
        )
        self.assertEqual(str_rep, str(new))

    @unittest.skipIf(storage != "db", "Testing if using DBStorage")
    def test_attr_(self):
        """ check attr on db"""

        new = self.value()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
