#!/usr/bin/python3
"""This module implements a "Base_Model" class

Usage:
    "BaseModel" class defines all common attributes/methods for other classes
    in the AirBnB clone console.
"""
import uuid
from datetime import datetime
from models import storage

iso_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Defines all common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Initializes instance of BaseModel.

        Attributes:
            id (str): Unique ID for each instance.
            created_at (datetime): assigns current datetime.
            updated_at (datetime): updates datetime when objects change.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, time)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Creates string representation of instance.

        Return:
            String representation of instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current
        datetime and saves the instances to a file.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Creates a dictionary containing all keys/values of __dict__ of the
        instance.

        Return:
            Dictionary containing all keys/values of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
