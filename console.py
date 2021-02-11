#!/usr/bin/python3
"""This module implements a "HBNBCommand" class

Usage:
    "HBNBCommand" contains the entry point of the command interpreter,
    uses the cmd module.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB console entry point"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the console"""
        print()
        return True

    def emptyline(self):
        """Doesn't execute anything when there is an empty line"""
        pass


if __name__ == '__main__':
    """Entry point"""
    interpreter = HBNBCommand()
    interpreter.cmdloop()
