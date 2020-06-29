#!/usr/bin/python3
"""
Module - File Storage
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file
    to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public instance method
        Returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Public instance method
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Public instance method
        Serializes __objects to the JSON file (path: __file_path)
        """
        item = {}
        for key in self.__objects:
            item[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as my_file:
            json.dump(item, my_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as my_file:
                item = json.load(my_file)
            for key in item:
                    self.__objects[key] = BaseModel(**item[key])
        except:
            pass
