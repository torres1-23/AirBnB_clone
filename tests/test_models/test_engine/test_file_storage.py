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


class TestFileStorage03(unittest.TestCase):
    """Check correct implementation of new(), save() and reload()
    method."""
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
        """Check correct implementation of save() method"""
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

    def test_08(self):
        """Check correct implementation of reload() method"""
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
        self.assertIn("BaseModel." + bm.id, self.obj_dict.keys())
        self.assertIn("User." + us.id, self.obj_dict.keys())
        self.assertIn("State." + st.id, self.obj_dict.keys())
        self.assertIn("Place." + pl.id, self.obj_dict.keys())
        self.assertIn("City." + cy.id, self.obj_dict.keys())
        self.assertIn("Amenity." + am.id, self.obj_dict.keys())
        self.assertIn("Review." + rv.id, self.obj_dict.keys())

    def test_09(self):
        """Check correct error Rises."""
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_11(self):
         """Check correct error Rises."""
        with self.assertRaises(AttributeError):
            storage.new(None)
        with self.assertRaises(TypeError):
            storage.save(None)
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_12(self):
        """Check correct error Rises."""
        self.assertRaises(FileNotFoundError, storage.reload())

    @classmethod
    def tearDown(self):
        try:
            os.remove("instance.json")
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
