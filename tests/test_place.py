#!/usr/bin/python3
"""
    place test module
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """place test class"""

    def test_init(self):
        """test initialisation"""
        place = Place()
        self.assertEqual("", place.name)
        self.assertEqual("", place.city_id)
        self.assertEqual("", place.user_id)
        self.assertEqual("", place.description)
        self.assertEqual(0, place.number_rooms)
        self.assertEqual(0, place.number_bathrooms)
        self.assertEqual(0, place.max_guest)
        self.assertEqual(0, place.price_by_night)
        self.assertEqual(0.0, place.latitude)
        self.assertEqual(0.0, place.longitude)
        self.assertEqual([], place.amenity_ids)

    def test_inherited_attr(self):
        """test inherited attributes"""
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))


if __name__ == "__main__":
    unittest.main()
