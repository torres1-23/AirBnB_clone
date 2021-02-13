#!/usr/bin/python3
"""This module implements a "Review" class that inherits
from "BaseModel" class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review instance."""
    place_id = ""
    user_id = ""
    text = ""
