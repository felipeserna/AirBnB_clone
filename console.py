#!/usr/bin/python3
"""
Module - console
"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    class console - entry point of the command interpreter
    """
    prompt = '(hbnb)'

    def do_EOF(self, args):
        """
        exit console - returns 0 on program success
        """
        return True

    def emptyline(self):
        """
        checks if no input given, an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_quit(self, args):
        """
        quit console - returns 0 on program success
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
