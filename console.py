#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
      """ Contains the functionality for the HBNB console"""

# determines prompt for interactive/non-interactive modes
prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

classes = {
'BaseModel': BaseModel
}

def preloop(self):
    """Prints if isatty is false"""
if not sys.__stdin__.isatty():
print('(hbnb)')

def precmd(self, line):
    """Reformat command line for advanced command syntax"""

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

def do_quit(self, command):
    """ Method to exit the HBNB console"""
exit()

def help_quit(self):
    """ Prints the help documentation for quit  """
print("Exits the program with formatting\n")

def do_EOF(self, arg):
    """ Handles EOF to exit program """
print()
exit()

def help_EOF(self):
    """ Prints the help documentation for EOF """
print("Exits the program without formatting\n")

def emptyline(self):
    """ Overrides the emptyline method of CMD """
pass

def do_create(self, args):
    """ Create an object of any class"""
if not args:
print("** class name missing **")
return

args = args.split()
class_name = args[0]

if class_name not in self.classes:
print("** class doesn't exist **")
return

new_instance = self.classes[class_name]()
storage.new(new_instance)
storage.save()
print(new_instance.id)

def help_create(self):
    """ Help information for the create method """
print("Creates a class of any type")
print("[Usage]: create <className>\n")

def do_show(self, args):
    """ Method to show an individual object """
if not args:
print("** class name missing **")
return

args = args.split()
class_name = args[0]

if class_name not in self.classes:
print("** class doesn't exist **")
return

if len(args) < 2:
print("** instance id missing **")
return

instance_id = args[1]
key = class_name + "." + instance_id

if key not in storage.all():
print("** no instance found **")
return

instance = storage.all()[key]
print(instance)

def help_show(self):
    """ Help information for the show command """
print("Shows an individual instance of a class")
print("[Usage]: show <className> <objectId>\n")

def do_destroy(self, args):
    """ Method to destroy an individual object """
if not args:
print("** class name missing **")
return

args = args.split()
class_name = args[0]

if class_name not in self.classes:
print("** class doesn't exist **")
return

if len(args) < 2:
print("** instance id missing **")
return

instance_id = args[1]
key = class_name + "." + instance_id

if key not in storage.all():
print("** no instance found **")
return

del storage.all()[key]
storage.save()

def help_destroy(self):
    """ Help information for the destroy command """
print("Destroys an instance of a class")
print("[Usage]: destroy <className> <objectId>\n")

def do_all(self, args):
    """ Method to print all instances """
if not args:
print([str(value) for value in storage.all().values()])
return

args = args.split()
class_name = args[0]

if class_name not in self.classes:
print("** class doesn't exist **")
return

print([str(value) for key, value in storage.all().items() if class_name in key])

def help_all(self):
    """ Help information for the all command """
print("Prints all instances")
print("[Usage]: all [<className>]\n")

def do_update(self, args):
    """ Method to update an instance attribute """
if not args:
print("** class name missing **")
return

args = args.split()
class_name = args[0]

if class_name not in self.classes:
print("** class doesn't exist **")
return

if len(args) < 2:
print("** instance id missing **")
return

instance_id = args[1]
key = class_name + "." + instance_id

if key not in storage.all():
print("** no instance found **")
return

if len(args) < 3:
print("** attribute name missing **")
return

if len(args) < 4:
print("** value missing **")
return

attribute_name = args[2]
attribute_value = args[3]

instance = storage.all()[key]
setattr(instance, attribute_name, attribute_value)
instance.save()

# Print the updated instance to confirm
print(instance)

def help_update(self):
    """ Help information for the update class """
print("Updates an object with new information")
print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
HBNBCommand().cmdloop()
