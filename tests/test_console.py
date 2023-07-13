#!/usr/bin/python3
"""
This module contains unit tests for the console.py file.
"""

import unittest
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """
    Test cases for the console.py file.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.console = HBNBCommand()
        self.output = StringIO()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.output.close()

    def test_quit(self):
        """
        Test the quit command.
        """
        self.assertTrue(self.console.onecmd('quit'))

    def test_eof(self):
        """
        Test the EOF command.
        """
        self.assertTrue(self.console.onecmd('EOF'))

    def test_emptyline(self):
        """
        Test the behavior of an empty line input.
        """
        self.assertIsNone(self.console.onecmd(''))

if __name__ == '__main__':
    unittest.main()
