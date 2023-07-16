#!/usr/bin/python3
"""
    city test module
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """city test class"""

    def test_init(self):
        """test initialisation"""
        city = City()
        self.assertEqual("", City.name)
        self.assertEqual("", City.state_id)

    def test_assign(self):
        """test assignments"""
        city = City()
        city.state_id = "12345"
        city.name = "Nigeria"
        self.assertEqual("12345", city.state_id)
        self.assertEqual("Nigeria", city.name)

    def test_inherited_attr(self):
        """test inherited attributes"""
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))


if __name__ == "__main__":
    unittest.main()
