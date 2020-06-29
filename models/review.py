#!/usr/bin/python3
"""
Module - review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    subclass - Review / inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public class attributes:
        text, place_id, text - string - empty strings
        """
        super().__init__(*args, **kwargs)
