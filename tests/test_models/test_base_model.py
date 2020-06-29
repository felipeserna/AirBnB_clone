#!/usr/bin/python3
"""Unittest for Base Model
"""
import unittest
import models
from models.base_model import BaseModel
import models.base_model
import json
import pep8
import sys
import io
from datetime import datetime
import inspect
import uuid
import time


class TestDocsBaseModel(unittest.TestCase):
    """SI FUNCIONAN LAS DE DOCUMENTACION
    check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8BaseModel(unittest.TestCase):
    """SI FUNCIONA
    check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBaseModel(unittest.TestCase):
    """
    tests class BaseModel
    """
    def test_init(self):
        """ No funciona
        checks correct instances """
        ww = BaseModel()
        ww.name = "waluigi"
        ww.my_number = 40
        a_t = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "my_number": int
            }
        for a, t in a_t.items():
            with self.subTest(a=a, t=t):
                self.assertIn(a, ww.__dict__)
                self.assertEqual(isinstance(ww.__dict__[a], t), True)
        self.assertEqual(ww.name, "waluigi")
        self.assertEqual(ww.my_number, 40)

    def test_save(self):
        """SI FUNCIONA
        check if last updated changes where saved"""
        hola = BaseModel()
        creado = hola.created_at
        viejo = hola.updated_at
        time.sleep(1)
        hola.save()
        nuevo = hola.updated_at
        self.assertNotEqual(viejo, nuevo)
        self.assertEqual(viejo, creado)
        self.assertNotEqual(nuevo, creado)

    def test_uuid(self):
        """SI FUNCIONA
        test valid uuid"""
        pepita = BaseModel()
        cholado = BaseModel()

        def is_valid_uuid(val):
            """check uuid"""
            try:
                uuid.UUID(str(val))
                return True
            except ValueError:
                return False
        self.assertEqual(is_valid_uuid(pepita.id), True)
        self.assertNotEqual(pepita.id, cholado.id)

    def test_to_dict(self):
        """SI FUNCIONA
        test to dictionary for json"""
        pipelin = BaseModel()
        pipelin.name = "felipe"
        pipelin.my_number = 5
        my_dictionary = pipelin.to_dict()
        expected = ["id", "created_at", "updated_at", "name", "my_number",
                    "__class__"]
        self.assertCountEqual(my_dictionary.keys(), expected)
        self.assertEqual(my_dictionary['__class__'], "BaseModel")
        self.assertEqual(my_dictionary['name'], "felipe")
        self.assertEqual(my_dictionary['my_number'], 5)

    def test_dict_dt_values(self):
        """
        check if attribute datetime values are in the correct output format
        """
        box = BaseModel()
        box.name = "Banana"
        box.my_number = 25
        d = box.to_dict()
        format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(isinstance(d["created_at"], str), True)
        self.assertEqual(isinstance(d["updated_at"], str), True)
        self.assertEqual(d["created_at"], box.created_at.strftime(format))
        self.assertEqual(d["updated_at"], box.updated_at.strftime(format))

    def test_datetime(self):
        """SI FUNCIONA
        check datetime values"""
        clock_one = datetime.now()
        one = BaseModel()
        clock_two = datetime.now()
        self.assertTrue(clock_one <= one.created_at <= clock_two)
        time.sleep(1)
        clock_one = datetime.now()
        two = BaseModel()
        clock_two = datetime.now()
        self.assertTrue(clock_one <= two.created_at <= clock_two)
        self.assertEqual(one.created_at, one.updated_at)
        self.assertEqual(two.created_at, two.updated_at)
        self.assertNotEqual(one.created_at, two.created_at)
        self.assertNotEqual(one.updated_at, two.updated_at)

    def test_str(self):
        """SI FUNCIONA
        test of str"""
        pepito = BaseModel()
        string = "[BaseModel] ({}) {}".format(pepito.id, pepito.__dict__)
        self.assertEqual(string, str(pepito))

if __name__ == '__main__':
    unittest.main()
