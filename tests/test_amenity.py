#!/usr/bin/python3
"""
    Amenity test module
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """amenity test class"""

    def test_init(self):
        """test initialisation"""
        amenity = Amenity()
        self.assertEqual("", amenity.name)

    def test_assign(self):
        """test assignments"""
        amenity = Amenity()
        amenity.name = "Nigeria"
        self.assertEqual("Nigeria", amenity.name)

    def test_inherited_attr(self):
        """test inherited attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_str_representation(self):
        amenity = Amenity()
        amenity.id = "123"
        amenity.name = "WiFi"
        amenity_str = (
                "[Amenity] (123) {'id': '123', 'created_at': " +
                repr(amenity.created_at) + ", 'updated_at': " +
                repr(amenity.updated_at) + ", 'name': 'WiFi'}"
                )
        self.assertEqual(amenity_str, str(amenity))


if __name__ == "__main__":
    unittest.main()
