#!/usr/bin/python3
"""Module for HBNB command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB project."""
    
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = args[0] + '.' + args[1]
        if key not in obj_dict:
            print("** no instance found **")
            return

        print(obj_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = args[0] + '.' + args[1]
        if key not in obj_dict:
            print("** no instance found **")
            return

        del obj_dict[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        obj_dict = storage.all()
        if not arg:
            print([str(obj) for obj in obj_dict.values()])
            return

        args = shlex.split(arg)
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in obj_dict.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = args[0] + '.' + args[1]
        if key not in obj_dict:
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
        obj = obj_dict[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
