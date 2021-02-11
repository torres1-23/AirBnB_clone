#!/usr/bin/python3
"""This module implements a "FileStorage" class

Usage:
    "FileStorage" class serializes instances to a JSON file and
    deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
    instances.
    """
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
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        dicti = FileStorage.__objects
        for key, value in dicti.items():
            dic = value.to_dict()
            new_dict[key] = dic
        with open(FileStorage.__file_path, "w", encoding='UTF8') as s_file:
            json.dump(new_dict, s_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding='UTF8') as s_file:
                FileStorage.__objects = json.load(s_file)
            for obj in FileStorage.__objects.values():
                self.new(BaseModel(**obj))
        except FileNotFoundError:
            return
