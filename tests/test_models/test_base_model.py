#!/usr/bin/python3
"""This module tests base_model.py file.

Usage:
    To be used with the unittest module:
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_models/test_base_model.py"
"""

import models
from models.base_model import BaseModel
import time
from time import sleep
import unittest
from unittest import mock
from datetime import datetime
import inspect
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModel01(unittest.TestCase):
    """Tests to check the documentation of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

        def test_func_docstrings(self):
            """Test for the presence of docstrings in BaseModel methods"""
            for func in self.base_funcs:
                with self.subTest(function=func):
                    self.assertIsNot(
                        func[1].__doc__,
                        None,
                        "{:s} method needs a docstring".format(func[0])
                    )
                    self.assertTrue(
                        len(func[1].__doc__) > 1,
                        "{:s} method needs a docstring".format(func[0])
                    )


class TestBaseModel02(unittest.TestCase):
    """Test the BaseModel class"""
    @mock.patch('models.storage')
    def test_instantiation(self, mock_storage):
        """Test that object is correctly created"""
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)
        inst.name = "Holberton"
        inst.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(inst.name, "Holberton")
        self.assertEqual(inst.number, 89)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


class TestBaseModel03(unittest.TestCase):
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
        """Checks for correct time stamps with update"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)
        sleep(2)
        base2.save()
        self.assertNotEqual(base2.created_at, base2.updated_at)


if __name__ == "__main__":
    unittest.main()
