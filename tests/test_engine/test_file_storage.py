#!/usr/bin/python3
"""
    unittest module for file_storage
"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """class for file_storage unittest"""

    @classmethod
    def setUpClass(cls):
        """test set up"""

        cls.file_path = "test_file.json"
        cls.storage = FileStorage()
        cls.storage._FileStorage__file_path = cls.file_path

    @classmethod
    def tearDownClass(cls):
        """after test clean up"""

        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

    def setUp(self):
        """set up"""

        self.storage._FileStorage__objects = {}

    def test_all(self):
        """test all method"""

        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """test new method"""

        bm = BaseModel()
        self.storage.new(bm)
        objects = self.storage.all()
        key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertIn(key, objects)

    def test_save(self):
        """test save method"""

        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """test reload method"""

        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        objects = new_storage.all()

        key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertIn(key, objects)

    def test_reload_creates_objects(self):
        """test reload method for created objects"""
        bm = BaseModel()
        user = User()
        self.storage.new(bm)
        self.storage.new(user)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        objects = new_storage.all()

        bm_key = f"{bm.__class__.__name__}.{bm.id}"
        user_key = f"{user.__class__.__name__}.{user.id}"
        self.assertIsInstance(objects[bm_key], BaseModel)
        self.assertIsInstance(objects[user_key], User)


if __name__ == "__main__":
    unittest.main()
