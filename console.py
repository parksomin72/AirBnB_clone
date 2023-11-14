# Add an extra blank line after class or function definitions
class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    
    prompt = '(hbnb) '
    
    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True

# Add an extra blank line between functions
def main():
    """Entry point of the command interpreter."""
    HBNBCommand().cmdloop()

if __name__ == '__main__':
    main()
