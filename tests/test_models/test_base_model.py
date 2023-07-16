#!/usr/bin/python3
"""
    Unnitest Module
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """TestBaseModel Class"""

    def test_init_attributes(self):
        """checks for init attributes"""

        bm = BaseModel()
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))

    def test_init_with_kwargs(self):
        """checks for init attribute with kwargs"""

        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_unique_id(self):
        """checks if ids are unique"""

        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_string_representation(self):
        """checks string representation of instance"""

        bm = BaseModel()
        bm.id = "123456"
        bm_str = str(bm)
        self.assertIn("[BaseModel] (123456)", bm_str)
        self.assertIn("'id': '123456'", bm_str)
        self.assertIn("'created_at': ", bm_str)
        self.assertIn("'updated_at': ", bm_str)

    def test_save(self):
        """test the save instance"""

        bm = BaseModel()
        original_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(original_updated_at, bm.updated_at)

    def test_to_dict_attr(self):
        """test to dictionary attributes"""

        bm = BaseModel()
        bm.name = "Test Model"
        bm.number = 100
        bm_dict = bm.to_dict()
        self.assertIn('id', bm_dict)
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)
        self.assertIn('__class__', bm_dict)
        self.assertIn('name', bm_dict)
        self.assertIn('number', bm_dict)

    def test_to_dict_str_attr(self):
        """test dictionary strings"""

        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)
        self.assertNotIsInstance(bm_dict['created_at'], datetime)
        self.assertNotIsInstance(bm_dict['updated_at'], datetime)


if __name__ == "__main__":
    unittest.main()
