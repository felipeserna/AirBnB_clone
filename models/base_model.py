#!/usr/bin/python3
"""
Module - Base Model
"""
import json
import uuid
from datetime import datetime


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    Private class attribute - ni (number of instances)
    """
    __ni_objects = 0

    def __init__(self, id=None, created_at, updated_at):
        """
        Initialize public class attributes:
        id - string - assign with an uuid when an instance is created.
        created_at - datetime - assign with the current datetime
        when an instance is created
        updated_at - datetime - assign with the current datetime when
        an instance is created and it will be updated every time you
        change your object
        """
        if id is not None:
            self.id = id
        else:
            BaseModel.__ni_objects += 1
            for i in __ni_objects:
                self.id = str(uuid.uuid4())

        if id is None:
            self.created_at = self.updated_at = datetime.utcnow()
            tmp = datetime.strptime(tmp, %Y-%m-%dT%H:%M:%S.%f)
        else:
            self.updated_at = datetime.utcnow()
