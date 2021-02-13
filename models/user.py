#!/usr/bin/python3
"""This module implements a "User" class that inherits
from "BaseModel" class.

Usage:
    "User" class represents a user instance.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User instance."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
