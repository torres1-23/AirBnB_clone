#!/usr/bin/python3
"""This module implements a "HBNBCommand" class

Usage:
    "HBNBCommand" contains the entry point of the command interpreter,
    uses the cmd module.
"""
import shlex
import cmd
from models.base_model import BaseModel
from models import storage

classes = {"BaseModel": BaseModel}
class_dict = storage.all()


def parsing(args):
    """Returns a parsed version of the args"""
    return shlex.split(args)


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

    def do_show(self, args):
        """[show <class name> <id>]: Prints an instance as a string"""
        arg = parsing(args)
        if len(arg[0]) == 0:
            print("** class name missing **")
        if arg[0] in classes.keys():
            if len(arg) == 2:
                key = arg[0] + "." + arg[1]
                if key in class_dict:
                    print(class_dict[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """[destroy <class name> <id>]: Deletes an instance"""
        arg = parsing(args)
        if len(arg[0]) == 0:
            print("** class name missing **")
        if arg[0] in classes.keys():
            if len(arg) == 2:
                key = arg[0] + "." + arg[1]
                if key in class_dict:
                    del(class_dict[key])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """[all <class name> / all]: Prints all string repr of all instances"""
        arg = parsing(args)
        list_all = []
        if len(arg) == 0:
            for value in class_dict.values():
                list_all.append(str(value))
            print(list_all)
        elif arg[0] in classes:
            for key in class_dict.keys():
                obj = class_dict[key]
                if arg[0] == obj.__class__.__name__:
                    list_all.append(str(obj))
            print(list_all)
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
