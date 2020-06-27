#!/usr/bin/python3
"""
Module - state
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    subclass - State / inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public class attribute:
        name - string - empty string
        """
        super().__init__(*args, **kwargs)
