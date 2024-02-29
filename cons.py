#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for Holberton School AirBnB project."""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all(class_name)
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all(class_name)
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = shlex.split(arg)
        if not args:
            all_objs = []
            for cls in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                all_objs.extend(str(obj) for obj in storage.all(cls).values())
            print(all_objs)
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        all_objs = storage.all(class_name)
        print([str(obj) for obj in all_objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all(class_name)
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = all_objs[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Handles empty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
