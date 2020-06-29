#!/usr/bin/python3
"""
test subclass User inherits from BaseModel
"""


from datetime import datetime
import unittest
import models
from models.base_model import BaseModel
from models import user
from models.user import User
import inspect
import pep8


class TestDocsUser(unittest.TestCase):
    """SI FUNCIONAN LAS DE DOCUMENTACION
    check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(models.user.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(User.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8User(unittest.TestCase):
    """SI FUNCIONA
    check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class testUser(unittest.TestCase):
    """
    tests subclass User
    """
    def test_subclass_of_BaseModel(self):
        """
        check if user inherits from BaseModel, check for the attributes
        """
        my_user = User()
        self.assertIsInstance(my_user, BaseModel)
        self.assertTrue(hasattr(my_user, "id"))
        self.assertTrue(hasattr(my_user, "created_at"))
        self.assertTrue(hasattr(my_user, "updated_at"))

    def test_User_attributes(self):
        """
        check if has attributes email, password, first & last names
        """
        new_user = User()
        self.assertTrue(hasattr(new_user, "email"))
        self.assertEqual(new_user.email, "")
        self.assertTrue(hasattr(new_user, "password"))
        self.assertEqual(new_user.password, "")
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertEqual(new_user.first_name, "")
        self.assertTrue(hasattr(new_user, "last_name"))
        self.assertEqual(new_user.last_name, "")

    def test_to_dict_user(self):
        """
        check if the dictionary is created
        with the correct attributes for datetime
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        holi = User()
        d = holi.to_dict()
        self.assertIsInstance(d, dict)
        for keys in d:
            self.assertTrue(keys, d)
            self.assertTrue('__class__' in d)
        self.assertEqual(d["__class__"], "User")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertEqual(d["created_at"], holi.created_at.strftime(format))
        self.assertEqual(d["updated_at"], holi.updated_at.strftime(format))

    def test_str_User(self):
        """
        check for correct informal string representation json of subclass user
        """
        ana = User()
        string = "[User] ({}) {}".format(ana.id, ana.__dict__)
        self.assertEqual(string, str(ana))

if __name__ == '__main__':
    unittest.main()
