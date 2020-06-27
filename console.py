#!/usr/bin/python3
"""
Module - console
"""

from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import models
import shlex
classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
ints = "number_rooms, number_bathrooms, max_guest, price_by_night"
floats = "latitude, longitud"
class HBNBCommand(cmd.Cmd):
    """
    class console - entry point of the command interpreter
    """
    prompt = '(hbnb)'

    def do_EOF(self, args):
        """
        public instance method
        exit console - returns 0 on program success
        """
        return True

    def emptyline(self):
        """
        public instance method
        checks if no input given, an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_quit(self, args):
        """
        public instance method
        quit console - returns 0 on program success
        """
        return True

    def do_create(self, args):
        """
        public instance method
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id.
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            instance = eval(args[0])()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, args):
        """
        public instance method
        Prints the string representation of an instance
        based on the class name and id
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]  #args 0 is name, args 1 es id
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        public instance method
        Deletes an instance based on the class name and id
        Save the change into the JSON file
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        public instance method
        Prints all string representation
        of all instances based or not on the class name.
        """
        args = shlex.split(args)
        if len(args) == 0:
            for item in models.storage.all():
                print(item)

        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    print(models.storage.all()[key])
                else:
                    print("** class doesn't exist **")
                    return False
        else:
            print("** class doesn't exist **")
            return False

    def do_update(self, args):
        """
        public instance method
        Updates an instance based on the class name and id
        by adding or updating attribute
        save the change into the JSON file
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            try:
                                if isinstance(args[2], datetime) is True:
                                    pass
                                if args[0] in classes:
                                    if isinstance(args[2], ints) is True:
                                        args[3] = int(args[3])
                                    elif isinstance(args[2], floats) is True:
                                        args[3] = float(args[3])
                            except:
                                pass
                            setattr(models.storage.all()[key], args[2], args[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
