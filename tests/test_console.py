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


class TestConsole_03(unittest.TestCase):
    """Checks help command"""
    def test_01(self):
        """Checks help alone"""
        help_str = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  count  create  destroy  help  quit  show  "
                    "update  update_dict")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_02(self):
        """Checks help EOF"""
        help_str = "EOF signal to exit the console."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_03(self):
        """Checks help all"""
        help_str = ("[all <class name> / all]: Prints all string repr of all "
                    "instances")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_04(self):
        """Checks help count"""
        help_str = ("[<class name>.count()]: Retrieves number of instances of "
                    "a class")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_05(self):
        """Checks help create"""
        help_str = "[create <class name>]: Creates a new instance of a class."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_06(self):
        """Checks help destroy"""
        help_str = "[destroy <class name> <id>]: Deletes an instance"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_07(self):
        """Checks help help"""
        help_str = ("List available commands with \"help\" or detailed help "
                    "with \"help cmd\".")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_08(self):
        """Checks help quit"""
        help_str = "[quit]: Exits the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_09(self):
        """Checks help show"""
        help_str = "[show <class name> <id>]: Prints an instance as a string"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_10(self):
        """Checks help update"""
        help_str = ("[update <class name> <id> <attribute name> \""
                    "<attribute value>\"]:\n"
                    "        Updates an attribute of an instance.\n"
                    "        [<class name>.update(<id>, <dictionary "
                    "representation>)]:\n"
                    "        Updates attributes of instance based on a "
                    "dictionary")

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(help_str, output.getvalue().strip())

    def test_11(self):
        """Checks help update_dict"""
        help_str = "Updates an instance based on id with dictionary"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update_dict"))
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


class TestConsole_05(unittest.TestCase):
    """Checks destroy command"""
    def test_01(self):
        """Checks destroy alone"""
        return_str = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(return_str, output.getvalue().strip())

    def test_02(self):
        """Checks destroy with no real class"""
        return_str = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy q"))
            self.assertEqual(return_str, output.getvalue().strip())

    def test_03(self):
        """Checks destroy with real class
        but no id"""
        return_str = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(return_str, output.getvalue().strip())

    def test_04(self):
        """Checks destroy with real class but wrong id"""
        return_str = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel a"))
            self.assertEqual(return_str, output.getvalue().strip())

    def test_05(self):
        """Checks right destruction of BaseModel instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            ids = output.getvalue().strip()
            self.assertIsNone(HBNBCommand().onecmd("destroy BaseModel " + ids))

    def test_06(self):
        """Checks right destruction of Amenity instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            ids = output.getvalue().strip()
            self.assertIsNone(HBNBCommand().onecmd("destroy Amenity " + ids))

    def test_07(self):
        """Checks right destruction of City instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            ids = output.getvalue().strip()
            self.assertIsNone(HBNBCommand().onecmd("destroy City " + ids))

    def test_08(self):
        """Checks right destruction of Place instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            ids = output.getvalue().strip()
            self.assertIsNone(HBNBCommand().onecmd("destroy Place " + ids))

    def test_09(self):
        """Checks right destruction of Review instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            ids = output.getvalue().strip()
            self.assertIsNone(HBNBCommand().onecmd("destroy Review " + ids))

    def test_10(self):
        """Checks right destruction of State instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            ids = output.getvalue().strip()
            self.assertIsNone(HBNBCommand().onecmd("destroy State " + ids))

    def test_11(self):
        """Checks right destruction of User instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            ids = output.getvalue().strip()
            self.assertIsNone(HBNBCommand().onecmd("destroy User " + ids))

    @classmethod
    def tearDown(self):
        """Deletes instance file."""
        try:
            os.remove("instance.json")
        except IOError:
            pass

if __name__ == "__main__":
    unittest.main()
