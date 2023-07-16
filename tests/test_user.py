#!/usr/bin/python3
"""
    user test module
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """user test class"""

    def test_init(self):
        """test initialisation"""
        user = User()
        self.assertEqual("", user.email)
        self.assertEqual("", user.password)
        self.assertEqual("", user.first_name)
        self.assertEqual("", user.last_name)

    def test_inherited_attr(self):
        """test inherited attributes"""
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))


if __name__ == "__main__":
    unittest.main()
