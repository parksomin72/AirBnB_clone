#!/usr/bin/python3
"""Command interpreter module"""
import cmd
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to JSON file"""
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
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()[args[0] + '.' + args[1]]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
            return
        if args[0] not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objs.items() if args[0] in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()[args[0] + '.' + args[1]]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], eval(args[3]))
        storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
