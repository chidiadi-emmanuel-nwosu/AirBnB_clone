#!/usr/bin/python3
"""
    Console Module
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class definition"""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }
    objs = storage.all()
    check_dict = 0

    def precmd(self, line):
        """parses input"""
        if '.' in line:
            if '{' in line or '}' in line:
                self.check_dict = 1
            else:
                self.check_dict = 0

            delim = '.(", :){}'
            get_input = re.split('[{}]+'.format(re.escape(delim)), line)
            res = get_input[1]

            for i in range(len(get_input) - 1):
                if i != 1:
                    res += " " + get_input[i].strip("'")

            return res
        else:
            return line

    def emptyline(self):
        """Prints an empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_create(self, line):
        """
        Creates a new instance of a class,
        saves it (to the JSON file) and prints the id
        Ex: $ create BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            new_ins = self.classes[line]()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                if args[0] not in self.classes.keys():
                    print("** class doesn't exist **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    if key in self.objs.keys():
                        print(self.objs[key])
                    else:
                        print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                if args[0] not in self.classes.keys():
                    print("** class doesn't exist **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    if key in self.objs.keys():
                        del self.objs[key]
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        Ex: $ all BaseModel or $ all
        """
        list_str = []
        if not line:
            list_str = [obj.__str__() for obj in self.objs.values()]
            print(list_str)
        else:
            if line not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                list_str = [
                        obj.__str__() for obj in self.objs.values()
                        if obj.__class__.__name__ == line
                        ]
                print(list_str)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com
        """
        args = line.split()

        if len(args) >= 4:
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                key = f"{args[0]}.{args[1]}"

                if key in self.objs.keys():
                    if self.check_dict == 1:
                        for i in range(2, len(args), 2):
                            setattr(self.objs[key], args[i], args[i + 1])
                    else:
                        args[2] = args[2].strip('"')
                        args[3] = args[3].strip('"')
                        setattr(self.objs[key], args[2], args[3])
                    self.objs[key].save()
                else:
                    print("** no instance found **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

        self.check_dict = 0

    def do_count(self, line):
        """retrieve the number of instances of a class"""
        count = 0

        for obj in self.objs.values():
            if obj.__class__.__name__ == line:
                count += 1

        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
