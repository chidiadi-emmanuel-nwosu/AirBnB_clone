#!/usr/bin/python3
"""
    review test module
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """review test class"""

    def test_init(self):
        """test initialisation"""
        review = Review()
        self.assertEqual("", review.place_id)
        self.assertEqual("", review.text)
        self.assertEqual("", review.user_id)

    def test_inherited_attr(self):
        """test inherited attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))


if __name__ == "__main__":
    unittest.main()
