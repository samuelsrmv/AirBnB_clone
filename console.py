#!/usr/bin/python3
"""The console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """[This is the htbn cls]
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit: quit
    Quit the console."""
        return True

    def do_EOF(self, arg):
        """EOF: ^C
    Exit the console."""
        return True


if __name__ == '__main__':
    """main entry"""
    HBNBCommand().cmdloop()
