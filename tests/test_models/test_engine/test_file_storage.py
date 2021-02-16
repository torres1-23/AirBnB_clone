#!/usr/bin/python3
"""This module tests file_storage.py file.

Usage:
    To be used with the unittest module, can be use it with
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_models/test_engine/test_file_storage.py"
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
        """Check correct with no arguments."""
        fs0 = FileStorage()
        self.assertEqual(type(fs0), FileStorage)

    def test_02(self):
        """Check correct priv class attr."""
        file_path = FileStorage._FileStorage__file_path
        self.assertEqual(type(file_path), str)

    def test_03(self):
        """Check correct priv class attr."""
        objects_dict = FileStorage._FileStorage__objects
        self.assertEqual(type(objects_dict), dict)

    def test_04(self):
        """Check correct storage instantiation."""
        self.assertEqual(type(storage), FileStorage)

    def test_05(self):
        """Check error raises."""
        with self.assertRaises(TypeError):
            FileStorage(None)


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


class TestFileStorage03(unittest.TestCase):
    """Check correct implementation of new(), save() and reload()
    method."""

    def test_01(self):
        """Check object type BaseModel newly created in __objects"""
        obj_dict = storage.all()
        bm1 = BaseModel()
        storage.new(bm1)
        key = "BaseModel." + bm1.id
        self.assertIn(key, obj_dict.keys())

    def test_02(self):
        """Check object type User newly created in __objects"""
        obj_dict = storage.all()
        u1 = User()
        storage.new(u1)
        key = "User." + u1.id
        self.assertIn(key, obj_dict.keys())

    def test_03(self):
        """Check object type State newly created in __objects"""
        obj_dict = storage.all()
        s1 = State()
        storage.new(s1)
        key = "State." + s1.id
        self.assertIn(key, obj_dict.keys())

    def test_04(self):
        """Check object type City newly created in __objects"""
        obj_dict = storage.all()
        c1 = City()
        storage.new(c1)
        key = "City." + c1.id
        self.assertIn(key, obj_dict.keys())

    def test_05(self):
        """Check object type Place newly created in __objects"""
        obj_dict = storage.all()
        p1 = Place()
        storage.new(p1)
        key = "Place." + p1.id
        self.assertIn(key, obj_dict.keys())

    def test_06(self):
        """Check object type Review newly created in __objects"""
        obj_dict = storage.all()
        r1 = Review()
        storage.new(r1)
        key = "Review." + r1.id
        self.assertIn(key, obj_dict.keys())

    def test_07(self):
        """Check object type Amenity newly created in __objects"""
        obj_dict = storage.all()
        a1 = Amenity()
        storage.new(a1)
        key = "Amenity." + a1.id
        self.assertIn(key, obj_dict.keys())

    def test_08(self):
        """Check correct implementation of save() method"""
        obj_dict = storage.all()
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        storage.save()
        with open("instance.json", "r") as sf:
            save_text = sf.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_09(self):
        """Check correct implementation of reload() method"""
        obj_dict = storage.all()
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + bm.id, obj_dict.keys())
        self.assertIn("User." + us.id, obj_dict.keys())
        self.assertIn("State." + st.id, obj_dict.keys())
        self.assertIn("Place." + pl.id, obj_dict.keys())
        self.assertIn("City." + cy.id, obj_dict.keys())
        self.assertIn("Amenity." + am.id, obj_dict.keys())
        self.assertIn("Review." + rv.id, obj_dict.keys())

    def test_10(self):
        """Check correct error Rises."""
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_11(self):
        """Check correct error Rises."""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_12(self):
        """Check correct error Rises."""
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_13(self):
        """Check correct error Rises."""
        self.assertRaises(FileNotFoundError, storage.reload())

    def test_14(self):
        """Check correct error Rises."""
        with self.assertRaises(AttributeError):
            storage.new([])

    @classmethod
    def tearDown(self):
        """Deletes instance file."""
        try:
            os.remove("instance.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}


if __name__ == "__main__":
    unittest.main()
