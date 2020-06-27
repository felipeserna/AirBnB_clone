#!/usr/bin/python3
"""
Module - amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    subclass - Amenity / inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public class attribute:
        name - string - empty string
        """
        super().__init__(*args, **kwargs)
