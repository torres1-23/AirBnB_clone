#!/usr/bin/python3
"""This module implements an "Amenity" class that inherits
from "BaseModel" class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity instance."""
    name = ""
