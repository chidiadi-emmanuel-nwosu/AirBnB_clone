#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program on EOF (Ctrl+D)
        """
        return True

    def help_quit(self):
        """
        Help message for the quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help message for the EOF command
        """
        print("Exit the program on EOF (Ctrl+D)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
