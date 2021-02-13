#!/usr/bin/python3
"""This module implements a "City" class that inherits
from "BaseModel" class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City instance."""
    state_id = ""
    name = ""
