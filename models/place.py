#!/usr/bin/python3
"""
Module - place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    subclass - Place / inherits from BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public class attributes:
        city_id, user_id, name, description, amenity_ids - string- empty strings
        number_rooms, number_bathrooms, max_guest, price_by_night - integers
        latitude, longitude - floats
        """
        super().__init__(*args, **kwargs)
