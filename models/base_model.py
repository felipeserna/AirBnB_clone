#!/usr/bin/python3
"""
Module - Base Model
"""


from datetime import datetime
import uuid
import models
f_t = "%Y-%m-%dT%H:%M:%S.%f"  # ISO time format


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize public class attributes:
        id - string - assign with an uuid when an instance is created.
        datetime objects:
        created_at -  assign  current datetime on instance creation
        updated_at - assign current datetime updated if object changes
        """
        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], f_t)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], f_t)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        override default private class method - __str__
        informal string representation of the BaseModel class
        returns - [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
        public class method - save
        updates the public class attribute updated_at with current datatime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        public class method - to_dict
        returns the dictionary representation of BaseModel class
        __class__ key set as holder for class name of the object
        display datetime format as:
        Year-Month-DayTHour:Minutes:Seconds.Milliseconds
        """

        d = self.__dict__.copy()
        d["created_at"] = d["created_at"].strftime(f_t)
        d["updated_at"] = d["updated_at"].strftime(f_t)
        d["__class__"] = self.__class__.__name__
        return d
