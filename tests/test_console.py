#!/usr/bin/python3
""" ALL THE TESTS"""
import unittest
import sys
from io import StringIO


class test_Console_(unittest.TestCase):
    """ UNITTEST USER"""
    def setUp(self):
        """SetUp method"""

        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        """TearDown method."""

        sys.stdout = self.backup
