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
from unittest.mock import create_autospec
import os
from io import StringIO
from unittest.mock import patch
import sys


class TestConsole01(unittest.TestCase):
    """Checks instantiation of HBNBCommand"""

    @classmethod
    def setUp(self):
        try:
            os.remove("instance.json")
        except Exception:
            pass

    def test_01(self):
        """Check right attributes"""
        prompt = HBNBCommand.prompt
        self.assertEqual(prompt, "(hbnb) ")
        self.assertEqual(type(prompt), str)

    def test_02(self):
        """Check right type of newly created obj"""
        console = HBNBCommand()
        self.assertEqual(type(console), HBNBCommand)


class TestConsole02(unittest.TestCase):
    """Checks exit commands"""
    def test_01(self):
        """Checks quit comand"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_02(self):
        """Checks EOF command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestConsole03(unittest.TestCase):
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


class TestConsole04(unittest.TestCase):
    """Tests stdin, create and exit"""
    def setUp(self):
        """Mocks stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """Tests create method"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """Tests exit method"""
        cmd = self.create()
        self.assertRaises(SystemExit, quit)


if __name__ == "__main__":
    unittest.main()
