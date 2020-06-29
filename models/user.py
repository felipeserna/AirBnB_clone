#!/usr/bin/python3
"""
Module - user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    subclass - User / inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public class attributes:
        email - string - empty string
        password - string - empty string
        first_name - string - empty string
        last_name - string - empty string
        """
        super().__init__(*args, **kwargs)
