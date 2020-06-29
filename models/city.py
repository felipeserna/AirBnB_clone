#!/usr/bin/python3
"""
Module - city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    subclass - City / inherits from BaseModel
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public class attributes:
        state_id, name - string - empty strings
        """
        super().__init__(*args, **kwargs)
