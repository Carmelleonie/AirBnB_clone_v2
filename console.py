#!/usr/bin/python3

import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


def tokenizer(txt):
    _dict = {}
    for arg in txt:
        if '=' in arg:
            args = arg.split('=', 1)
            k = args[0]
            v = args[1]
            if v and len(v) > 1 and v[0] == v[1] == '"':
                v = split(v)[0].replace("_", " ")
            else:
                if '.' in v:
                   try:
                       v = int(v)
                   except:
                       continue
                else:
                    try:
                        v = float(v)
                    except:
                        continue
        _dict[k] = v
    return _dict


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    __type_of_class = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER"""
        pass

    def do_create(self, line):
        
        arg_list = line.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__type_of_class:
            print("** class doesn't exist **")
        else:
            class_name = arg_list[0]
            _dict = tokenizer(arg_list[1:])
            instance = HBNBCommand.__type_of_class[class_name](**_dict)
            print(instance.id)
            storage.save()

    def do_show(self, line):
        tokens = tokenizer(line)

        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif f"{tokens[0]}.{tokens[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(tokens[0], tokens[1])])

    def do_destroy(self, line):
        tokens = tokenizer(line)

        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] not in HBNBCommand.__type_of_class:
            print("** class doesn't exist **")
        elif f"{tokens[0]}.{tokens[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{tokens[0]}.{tokens[1]}"]
            storage.save()

    def do_all(self, line):
        tokens = tokenizer(line)

        _list = []
        if len(tokens) > 0 and tokens[0] not in HBNBCommand.__type_of_class:
            print("** class doesn't exist **")
        else:
            for element in storage.all().values():
                if len(tokens) and tokens[0] in HBNBCommand.__type_of_class:
                    _list.append(element.__str__())
                if len(tokens) == 0:
                    _list.append(element.__str__())
        print(_list)

    def do_update(self, line):
        tokens = tokenizer(line)

        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] not in HBNBCommand.__type_of_class:
            print("** class doesn't exist **")
        elif f"{tokens[0]}.{tokens[1]}" not in storage.all():
            print("** no instance found **")
        elif len(tokens) == 3:
            print("** value missing **")
        elif len(tokens) > 3:
            dict_r = storage.all()["{}.{}".format(tokens[0], tokens[1])]
            setattr(dict_r, tokens[2], tokens[3])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
