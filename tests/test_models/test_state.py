#!/usr/bin/python3
"""
test subclass State inherits from BaseModel
"""


from datetime import datetime
import unittest
import models
from models.base_model import BaseModel
from models import state
from models.state import State
import inspect
import pep8


class TestDocsState(unittest.TestCase):
    """SI FUNCIONAN LAS DE DOCUMENTACION
    check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(models.state.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(State.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8State(unittest.TestCase):
    """SI FUNCIONA
    check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/state.py'
        file2 = 'tests/test_models/test_state.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class testState(unittest.TestCase):
    """
    tests subclass State
    """
    def test_subclass_of_BaseModel(self):
        """
        check if State inherits from BaseModel, check for the attributes
        """
        my_state = State()
        self.assertIsInstance(my_state, BaseModel)
        self.assertTrue(hasattr(my_state, "id"))
        self.assertTrue(hasattr(my_state, "created_at"))
        self.assertTrue(hasattr(my_state, "updated_at"))

    def test_State_attributes(self):
        """
        check if has attributes email, password, first & last names
        """
        new_state = State()
        self.assertTrue(hasattr(new_state, "name"))
        self.assertEqual(new_state.name, "")

    def test_to_dict_state(self):
        """
        check if the dictionary is created
        with the correct attributes for datetime
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        holi = State()
        d = holi.to_dict()
        self.assertIsInstance(d, dict)
        for keys in d:
            self.assertTrue(keys, d)
            self.assertTrue('__class__' in d)
        self.assertEqual(d["__class__"], "State")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertEqual(d["created_at"], holi.created_at.strftime(format))
        self.assertEqual(d["updated_at"], holi.updated_at.strftime(format))

    def test_str_State(self):
        """
        check for correct informal string representation json of subclass State
        """
        kansas = State()
        string = "[State] ({}) {}".format(kansas.id, kansas.__dict__)
        self.assertEqual(string, str(kansas))
