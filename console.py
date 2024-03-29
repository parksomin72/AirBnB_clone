#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax."""
        if '.' in line and '(' in line and ')' in line:
            parts = line.split('.')
            command = parts[1].split('(')[0]
            args = parts[1].split('(')[1][:-1]
            return "{} {} {}".format(command, parts[0], args)
        return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Overrides the default emptyline behavior"""
        pass

    def do_create(self, args):
        """Create a new instance of a class"""
        args_list = split(args)
        if len(args_list) == 0:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Show details of a specific instance"""
        args_list = split(args)
        if len(args_list) == 0:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)
        obj = storage.all()
        if key in obj:
            print(obj[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Delete a specific instance"""
        args_list = split(args)
        if len(args_list) == 0:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)
        obj = storage.all()
        if key in obj:
            del obj[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Show all instances or instances of a specific class"""
        args_list = split(args)
        obj = storage.all()
        if len(args_list) == 0:
            print([str(v) for v in obj.values()])
        elif args_list[0] in self.classes:
            print([str(v) for k, v in obj.items() if args_list[0] in k])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update an instance with new information"""
        args_list = split(args)
        if len(args_list) == 0:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)
        obj = storage.all()
        if key not in obj:
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        if len(args_list) < 4:
            print("** value missing **")
            return

        setattr(obj[key], args_list[2], args_list[3])
        storage.save()

    def do_count(self, args):
        """Count instances of a specific class"""
        args_list = split(args)
        count = 0
        obj = storage.all()
        if len(args_list) == 0:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        for k in obj.keys():
            if class_name in k:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
