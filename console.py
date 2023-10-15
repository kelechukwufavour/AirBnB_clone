#!/usr/bin/python3
"""Defines the HBnB console"""

import cmd
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): command prompt.
    """

    prompt = "(hbnb) " 
    __classes = ["BaseModel", "User"]

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program
        """
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
