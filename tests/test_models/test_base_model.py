#!/usr/bin/python3
"""This module tests base_model.py file.

Usage:
    To be used with the unittest module, can be use it with
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_models/test_base_model.py"
"""
from models.base_model import BaseModel
import unittest


class TestBase01(unittest.TestCase):
    """Check instantiation of BaseModel instances."""
    def test_01(self):
        """Checks right instantiation of BaseModel"""
        base1 = BaseModel()
        self.assertEqual(base1.__class__.__name__, 'BaseModel')
        self.assertEqual(type(base1), BaseModel)
        base1.name = "Holberton"
        base1.number = "89"
        self.assertEqual(base1.name, "Holberton")
        self.assertEqual(base1.number, "89")

    def test_02(self):
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)
        sleep(2)
        base2.save()
        self.assertNotEqual(base2.created_at, base2.updated_at)
