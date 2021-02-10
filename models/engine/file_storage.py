#!/usr/bin/python3
"""This module implements a "FileStorage" class

Usage:
    "FileStorage" class serializes instances to a JSON file and
    deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """"""
    __file_path = "instance.json"
    __objects = {}

    def all(self):
        """Gets the dictionary of objects

        Return:
            Dictionary of objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding='UTF8') as s_file:
            json.dump(FileStorage.__objects, s_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding='UTF8') as s_file:
                FileStorage.__objects = json.load(s_file)
            for value in FileStorage.__objects:
                BaseModel.__init__(value)
        except FileNotFoundError:
            return
