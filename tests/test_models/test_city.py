#!/usr/bin/python3
"""
test subclass City inherits from BaseModel
"""


from datetime import datetime
import unittest
import models
from models.base_model import BaseModel
from models import city
from models.city import City
import inspect
import pep8
import sys
import os


class TestDocsCity(unittest.TestCase):
    """SI FUNCIONAN LAS DE DOCUMENTACION
    check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(models.city.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(City.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8City(unittest.TestCase):
    """SI FUNCIONA
    check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class testCity(unittest.TestCase):
    """
    tests subclass City
    """
    def tearDown(self):
        """clean everything up after running setup"""
        sys.stdout = sys.__stdout__
        os.remove("file.json")

    def test_subclass_of_BaseModel(self):
        """
        check if City inherits from BaseModel, check for the attributes
        """
        my_city = City()
        self.assertIsInstance(my_city, BaseModel)
        self.assertTrue(hasattr(my_city, "id"))
        self.assertTrue(hasattr(my_city, "created_at"))
        self.assertTrue(hasattr(my_city, "updated_at"))

    def test_City_attributes(self):
        """
        check if has attributes state_id & name
        """
        new_city = City()
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertTrue(hasattr(new_city, "name"))

    def test_to_dict_city(self):
        """
        check if the dictionary is created
        with the correct attributes for datetime
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        holi = City()
        d = holi.to_dict()
        self.assertIsInstance(d, dict)
        for keys in d:
            self.assertTrue(keys, d)
            self.assertTrue('__class__' in d)
        self.assertEqual(d["__class__"], "City")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertEqual(d["created_at"], holi.created_at.strftime(format))
        self.assertEqual(d["updated_at"], holi.updated_at.strftime(format))

    def test_str_City(self):
        """
        check for correct informal string representation json of subclass City
        """
        kansas = City()
        string = "[City] ({}) {}".format(kansas.id, kansas.__dict__)
        self.assertEqual(string, str(kansas))

if __name__ == '__main__':
    unittest.main()
