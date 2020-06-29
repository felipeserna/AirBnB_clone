#!/usr/bin/python3
"""
test subclass Amenity inherits from BaseModel
"""


from datetime import datetime
import unittest
import models
from models.base_model import BaseModel
from models import amenity
from models.amenity import Amenity
import inspect
import pep8


class TestDocsAmenity(unittest.TestCase):
    """SI FUNCIONAN LAS DE DOCUMENTACION
    check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(models.amenity.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8Amenity(unittest.TestCase):
    """SI FUNCIONA
    check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class testAmenity(unittest.TestCase):
    """
    tests subclass Amenity
    """
    def test_subclass_of_BaseModel(self):
        """
        check if Amenity inherits from BaseModel, check for the attributes
        """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, BaseModel)
        self.assertTrue(hasattr(my_amenity, "id"))
        self.assertTrue(hasattr(my_amenity, "created_at"))
        self.assertTrue(hasattr(my_amenity, "updated_at"))

    def test_Amenity_attributes(self):
        """
        check if has attributes email, password, first & last names
        """
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, "name"))
        self.assertEqual(new_amenity.name, "")

    def test_to_dict_amenity(self):
        """
        check if the dictionary is created
        with the correct attributes for datetime
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        holi = Amenity()
        d = holi.to_dict()
        self.assertIsInstance(d, dict)
        for keys in d:
            self.assertTrue(keys, d)
            self.assertTrue('__class__' in d)
        self.assertEqual(d["__class__"], "Amenity")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertEqual(d["created_at"], holi.created_at.strftime(format))
        self.assertEqual(d["updated_at"], holi.updated_at.strftime(format))

    def test_str_Amenity(self):
        """
        check for correct informal string representation json of subclass Amenity
        """
        kansas = Amenity()
        string = "[Amenity] ({}) {}".format(kansas.id, kansas.__dict__)
        self.assertEqual(string, str(kansas))
