#!/usr/bin/python3
"""
test subclass Review inherits from BaseModel
"""


from datetime import datetime
import unittest
import models
from models.base_model import BaseModel
from models import review
from models.review import Review
import inspect
import pep8


class TestDocsReview(unittest.TestCase):
    """SI FUNCIONAN LAS DE DOCUMENTACION
    check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(models.review.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8Review(unittest.TestCase):
    """SI FUNCIONA
    check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class testReview(unittest.TestCase):
    """
    tests subclass Review
    """
    def test_subclass_of_BaseModel(self):
        """
        check if Review inherits from BaseModel, check for the attributes
        """
        my_review = Review()
        self.assertIsInstance(my_review, BaseModel)
        self.assertTrue(hasattr(my_review, "id"))
        self.assertTrue(hasattr(my_review, "created_at"))
        self.assertTrue(hasattr(my_review, "updated_at"))

    def test_Review_attributes(self):
        """
        check if has attributes email, password, first & last names
        """
        new_review = Review()
        self.assertTrue(hasattr(new_review, "place_id"))
        self.assertTrue(hasattr(new_review, "user_id"))
        self.assertTrue(hasattr(new_review, "text"))

    def test_to_dict_review(self):
        """
        check if the dictionary is created
        with the correct attributes for datetime
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        holi = Review()
        d = holi.to_dict()
        self.assertIsInstance(d, dict)
        for keys in d:
            self.assertTrue(keys, d)
            self.assertTrue('__class__' in d)
        self.assertEqual(d["__class__"], "Review")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        self.assertEqual(d["created_at"], holi.created_at.strftime(format))
        self.assertEqual(d["updated_at"], holi.updated_at.strftime(format))

    def test_str_Review(self):
        """
        check correct informal string representation json of subclass Review
        """
        kansas = Review()
        string = "[Review] ({}) {}".format(kansas.id, kansas.__dict__)
        self.assertEqual(string, str(kansas))
