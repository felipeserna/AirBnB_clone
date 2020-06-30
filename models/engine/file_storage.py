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
l_c = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
       "Place": Place, "Review": Review, "State": State, "User": User}


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
        i = items , objects loaded
        k = keys , attribute names loaded
        there is a double pointer to asign values to those attributes
        """
        try:
            with open(self.__file_path, 'r') as my_file:
                i = json.load(my_file)
            for k in i:
                self.__objects[k] = l_C[i[k]["__class__"]](**i[k])
        except:
            pass
