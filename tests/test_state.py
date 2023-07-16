#!/usr/bin/python3
"""
    state test module
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """state test class"""

    def test_init(self):
        """test initialisation"""
        state = State()
        self.assertEqual("", state.name)

    def test_inherited_attr(self):
        """test inherited attributes"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))


if __name__ == "__main__":
    unittest.main()
