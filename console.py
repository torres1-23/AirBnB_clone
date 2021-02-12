#!/usr/bin/python3
"""This module implements a "HBNBCommand" class

Usage:
    "HBNBCommand" contains the entry point of the command interpreter,
    uses the cmd module.
"""
import cmd
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """HBNB console entry point"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """[create <class name>]: Creates a new instance of a class."""
        if len(args) == 0:
            print("** class name missing **")
        elif args in classes.keys():
            instance = classes[args]()
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """[quit]: Exits the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the console."""
        print()
        return True

    def emptyline(self):
        """Doesn't execute anything when there is an empty line"""
        pass


if __name__ == '__main__':
    """Entry point"""
    interpreter = HBNBCommand()
    interpreter.cmdloop()
