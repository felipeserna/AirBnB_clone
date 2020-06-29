#!/usr/bin/python3
"""
test subclass Place inherits from BaseModel
"""


from datetime import datetime
import unittest
import models
from models.base_model import BaseModel
from models import place
from models.place import Place
import inspect
import pep8


class TestDocsPlace(unittest.TestCase):
    """SI FUNCIONAN LAS DE DOCUMENTACION
    check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(models.place.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8Place(unittest.TestCase):
    """SI FUNCIONA
    check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class testPlace(unittest.TestCase):
    """
    tests subclass Place
    """
    def test_subclass_of_BaseModel(self):
        """
        check if Place inherits from BaseModel, check for the attributes
        """
        my_place = Place()
        self.assertIsInstance(my_place, BaseModel)
        self.assertTrue(hasattr(my_place, "id"))
        self.assertTrue(hasattr(my_place, "created_at"))
        self.assertTrue(hasattr(my_place, "updated_at"))

    def test_Place_attributes(self):
        """
        check if has attributes city_id, user_id, name, description,
        number_rooms, number_bathrooms, max_guest, price_by_night,
        latitude, longitude, amenity_ids
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "city_id"))
        self.assertTrue(hasattr(new_place, "user_id"))
        self.assertTrue(hasattr(new_place, "name"))
        self.assertTrue(hasattr(new_place, "description"))
        self.assertTrue(hasattr(new_place, "number_rooms"))
        self.assertTrue(hasattr(new_place, "number_bathrooms"))
        self.assertTrue(hasattr(new_place, "max_guest"))
        self.assertTrue(hasattr(new_place, "price_by_night"))
        self.assertTrue(hasattr(new_place, "latitude"))
        self.assertTrue(hasattr(new_place, "longitude"))
        self.assertTrue(hasattr(new_place, "amenity_ids"))

    def test_to_dict_place(self):
        """
        check if the dictionary is created
        with the correct attributes for datetime
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        holi = Place()
        d = holi.to_dict()
        self.assertIsInstance(d, dict)
        for keys in d:
            self.assertTrue(keys, d)
            self.assertTrue('__class__' in d)
        self.assertEqual(d["__class__"], "Place")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertEqual(d["created_at"], holi.created_at.strftime(format))
        self.assertEqual(d["updated_at"], holi.updated_at.strftime(format))

    def test_str_Place(self):
        """
        check correct informal string representation json of subclass Place
        """
        kansas = Place()
        string = "[Place] ({}) {}".format(kansas.id, kansas.__dict__)
        self.assertEqual(string, str(kansas))

if __name__ == '__main__':
    unittest.main()
