#!/usr/bin/python3
"""This module tests State.py file.
Usage:
    To be used with the unittest module:
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_models/test_state.py"
"""

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import unittest
import os
State = state.State


class TestState01(unittest.TestCase):
    """Tests to check the documentation of State class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_state_module_docstring(self):
        """Test for the state.py module docstring"""
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_state_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_func_docstrings(self):
        """Test for the presence of docstrings in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestState02(unittest.TestCase):
    """Test the State class"""
    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name_attr(self):
        """Test that State has attribute name, and it's as an empty string"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in s.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))


class TestState03(unittest.TestCase):
    """Test the State class"""
    @classmethod
    def setUpClass(cls):
        """Defines State and name"""
        cls.state1 = State()
        cls.state1.name = "California"

    @classmethod
    def tearDownClass(cls):
        """Deletes previously creates State and name attributes"""
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_checking_for_functions(self):
        """Checks if function exists"""
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """Checks for attributes"""
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributes_are_strings(self):
        """Checks if attributes are strings"""
        self.assertEqual(type(self.state1.name), str)

    def test_save(self):
        """Checks if State class is stored"""
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        """Test if State is instanced as a dict"""
        self.assertEqual('to_dict' in dir(self.state1), True)


if __name__ == "__main__":
    unittest.main()
