#!/usr/bin/python3
"""This module implements a "HBNBCommand" class

Usage:
    "HBNBCommand" contains the entry point of the command interpreter,
    uses the cmd module.
"""
from shlex import split
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.engine.file_storage import classes

class_dict = storage.all()


def parsing(args):
    """Returns a parsed version of the args"""
    return split(args)


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
        if len(arg) == 0:
            print("** class name missing **")
            return
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
        if len(arg) == 0:
            print("** class name missing **")
            return
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
        list_all = []
        if not args:
            for value in class_dict.values():
                list_all.append(str(value))
            print(list_all)
        elif args in classes:
            for key in class_dict.keys():
                obj = class_dict[key]
                if args == obj.__class__.__name__:
                    list_all.append(str(obj))
            print(list_all)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """[update <class name> <id> <attribute name> "<attribute value>"]:
        Updates an attribute of an instance.
        [<class name>.update(<id>, <dictionary representation>)]:
        Updates attributes of instance based on a dictionary"""
        try:
            arg = parsing(args)
            integers = ["number_rooms", "number_bathrooms", "max_guest",
                        "price_by_night"]
            floats = ["latitude", "longitude"]

            try:
                if arg[0] in classes.keys():
                    key = arg[0] + "."
                else:
                    print("** class doesn't exist **")
                    return
            except IndexError:
                print("** class name missing **")
                return
            try:
                key += arg[1]
                if key in class_dict:
                    obj = class_dict[key]
                else:
                    print("** no instance found **")
                    return
            except IndexError:
                print("** instance id missing **")
                return
            if len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                if arg[2] in integers:
                    try:
                        arg[3] = int(arg[3])
                    except:
                        print("*** Unknown syntax: {}".format(arg[3]))
                if arg[2] in floats:
                    try:
                        arg[3] = float(arg[3])
                    except:
                        print("*** Unknown syntax: {}".format(arg[3]))
                setattr(obj, arg[2], arg[3])
                storage.save()
        except ValueError:
            print("*** Unknown syntax: {}".format(args))

    def do_update_dict(self, args):
        """Updates an instance based on id with dictionary"""
        parse_braces = args.split("{")
        class_id = parse_braces[0]
        dict_to_parse = parse_braces[1]
        dict_to_parse = dict_to_parse[:-1]
        dict_to_parse = dict_to_parse.split(",")
        for element in dict_to_parse:
            name_value = element.split(":")
            string = class_id + " ".join(name_value)
            self.do_update(string)

    def do_count(self, args):
        """[<class name>.count()]: Retrieves number of instances of a class"""
        count = 0
        if args in classes:
            for obj in class_dict.values():
                if args == obj.__class__.__name__:
                    count += 1
        print(count)

    def do_quit(self, args):
        """[quit]: Exits the program."""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the console."""
        print()
        return True

    def emptyline(self):
        """Doesn't execute anything when there is an empty line"""
        pass

    def precmd(self, args):
        """Parses alternative input format"""
        open_par = args.count("(")
        closed_par = args.count(")")
        open_braces = args.count("{")
        closed_braces = args.count("}")
        if open_par == 1 and closed_par == 1:
            parse_dot = args.split(".")
            class_name = parse_dot[0]
            cmd_attributes = parse_dot[1]
            parse_par = cmd_attributes.split("(")
            command = parse_par[0]
            arg_par = parse_par[1]
            arg_nopar = arg_par[:-1]
            parse_args = split(arg_nopar)
            if command != "update":
                return command + " " + class_name + " " + " ".join(parse_args)
            else:
                if open_braces == 1 and closed_braces == 1:
                    command += '_dict'
                    id_string = parse_args[0][:-1]
                    return (command + " " + class_name + " " + id_string +
                            " " + " ".join(parse_args[1:]))
                elif len(parse_args) == 3:
                    value = parse_args[-1]
                    arg_string = " ".join(parse_args[:2])
                    arguments = arg_string.split(",")
                    return (command + " " + class_name + " " +
                            " ".join(arguments) + '"' + value + '"')
                else:
                    arg_string = " ".join(parse_args)
                    arguments = arg_string.split(", ")
                    return (command + " " + class_name + " " +
                            " ".join(arguments))
        else:
            return args


if __name__ == '__main__':
    """Entry point"""
    interpreter = HBNBCommand()
    interpreter.cmdloop()
