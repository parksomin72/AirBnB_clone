#!/usr/bin/python3
"""Console module for the AirBnB command interpreter."""
import cmd

class Console(cmd.Cmd):
    """Console class for AirBnB command interpreter."""

    prompt = "(hbnb) "

    def do_help(self, arg):
        """Display help information."""
        cmd.Cmd.do_help(self, arg)

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_EOF(self, line):
        """Exit on EOF."""
        print("")
        return True

if __name__ == "__main__":
    console = Console()
    console.cmdloop()
