#!/usr/bin/python3
"""This module tests file_storage.py file.

Usage:
    To be used with the unittest module, can be use it with
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_models/test_file_storage.py"
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import unittest
import os
import json


class TestFileStorage01(unittest.TestCase):
    """Test instantiation of FileStorage."""
    def test_01(self):
        fs0 = FileStorage()
        self.assertEqual(type(fs0), FileStorage)

    def test_02(self):
        """Check correct priv class attr."""
        file_path = FileStorage._FileStorage__file_path
        objects_dict = FileStorage._FileStorage__objects
        self.assertEqual(type(file_path), str)
        self.assertEqual(file_path, "instance.json")
        self.assertEqual(type(objects_dict), dict)

    def test_03(self):
        """Check correct storage instantiation."""
        self.assertEqual(type(storage), FileStorage)

    def test_04(self):
        """Check error raises."""
        with self.assertRaises(TypeError):
            fs1 = FileStorage(1)


class TestFileStorage02(unittest.TestCase):
    """Check correct implementation of all() method."""
    def test_01(self):
        """Check correct type of dict."""
        dictionary = storage.all()
        self.assertEqual(type(dictionary), dict)

    def test_02(self):
        """Check error raises."""
        with self.assertRaises(TypeError):
            dictionary = storage.all(None)

    @classmethod
    def tearDown(self):
        try:
            os.remove("instance.json")
        except IOError:
            pass


class TestFileStorage03(unittest.TestCase):
    """Check correct implementation of new() method."""
    obj_dict = storage.all()

    def test_01(self):
        """Check object type BaseModel newly created in __objects"""
        bm1 = BaseModel()
        storage.new(bm1)
        key = "BaseModel." + bm1.id
        self.assertIn(key, self.obj_dict.keys())

    def test_02(self):
        """Check object type User newly created in __objects"""
        u1 = User()
        storage.new(u1)
        key = "User." + u1.id
        self.assertIn(key, self.obj_dict.keys())

    def test_03(self):
        """Check object type State newly created in __objects"""
        s1 = State()
        storage.new(s1)
        key = "State." + s1.id
        self.assertIn(key, self.obj_dict.keys())

    def test_04(self):
        """Check object type City newly created in __objects"""
        c1 = City()
        storage.new(c1)
        key = "City." + c1.id
        self.assertIn(key, self.obj_dict.keys())

    def test_05(self):
        """Check object type Place newly created in __objects"""
        p1 = Place()
        storage.new(p1)
        key = "Place." + p1.id
        self.assertIn(key, self.obj_dict.keys())

    def test_06(self):
        """Check object type Review newly created in __objects"""
        r1 = Review()
        storage.new(r1)
        key = "Review." + r1.id
        self.assertIn(key, self.obj_dict.keys())

    def test_07(self):
        """Check correct error Rises."""
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    @classmethod
    def tearDown(self):
        try:
            os.remove("instance.json")
        except IOError:
            pass


class TestFileStorage04(unittest.TestCase):
    """Check correct implementation of save() method."""
    def test_01(self):
        pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("instance.json")
        except IOError:
            pass
