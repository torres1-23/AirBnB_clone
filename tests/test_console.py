#!/usr/bin/python3
"""This module tests console.py file.
Usage:
    To be used with the unittest module, can be use it with
    "python3 -m unittest discover tests" command or
    "python3 -m unittest tests/test_console.py"
"""
from models.engine.file_storage import FileStorage
from models import storage
from console import HBNBCommand
import unittest
import os
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_01(unittest.TestCase):
    """Checks instantiation of HBNBCommand"""
    def test_01(self):
        """Check right attributes"""
        prompt = HBNBCommand.prompt
        self.assertEqual(prompt, "(hbnb) ")
        self.assertEqual(type(prompt), str)

    def test_02(self):
        """Check right type of newly created obj"""
        console = HBNBCommand()
        self.assertEqual(type(console), HBNBCommand)


class TestHBNBCommand_02(unittest.TestCase):
    """Checks exit commands"""
    def test_01(self):
        """Checks quit comand"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_02(self):
        """Checks EOF command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_03(unittest.TestCase):
    """Checks help command"""
    def test_01(self):
        """Tests for correct help output"""
        help_str = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  count  create  destroy  help  quit  show  "
                    "update  update_dict")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help_str, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
