#!/usr/bin/python3
"""
This is the console model.
It provides an entry to the console with
some specific implementations.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """It provides the entry point to the interpreter."""

    prompt = "(hbnb) "
    my_classes = {"BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"}

    def do_quit(self, s):
        """This implements the quit command."""
        return True

    def do_EOF(self, s):
        """This implements the EOF command."""
        print()
        return True

    def help_quit(self):
        """This implements the help for the quit command."""
        print("Quit command to exit the program.\n")

    def help_EOF(self):
        """This implements the help for the EOF command."""
        print("EOF command to exit the program.\n")

    def emptyline(self):
        """This overrides the default empty line method."""
        pass

    def do_create(self, s):
        """Create a new instance of BaseModel, save it, and print the id."""
        if len(s) == 0:
            print("** class name missing **")
        elif s not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(s)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, s):
        """Print the string representation of an instance."""
        if len(s) == 0:
            print("** class name missing **")
            return
        args = list(s.split())
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        try:
            classname = f"{args[0]}.{args[1]}"
            if classname not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[classname])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, s):
        """Delete an instance based on the class name and id."""
        if len(s) == 0:
            print("** class name missing **")
            return
        args = list(s.split())
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        try:
            classname = f"{args[0]}.{args[1]}"
            if classname not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[classname]
                storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, s):
        """Print all objects or objects of a particular class."""
        obj_lists = []
        args = list(s.split())
        if len(s) == 0:
            for keys in storage.all().values():
                obj_lists.append(keys)
            print(obj_lists)
        elif s in HBNBCommand.my_classes:
            for key, value in storage.all().items():
                if s in key:
                    obj_lists.append(value)
            print(obj_lists)
        else:
            print("** class doesn't exist **")

    def do_update(self, s):
        """Update an instance based on the class name and id."""
        args = list(s.split())
        obj_dict = storage.all()
        if len(args) >= 4:
            classname = f"{args[0]}.{args[1]}"
            attr_value = args[3]
            attr_value = attr_value.strip('"')
            attr_value = attr_value.strip("'")
            casting = type(eval(args[3]))
            setattr(storage.all()[classname], args[2], casting(attr_value))
            storage.all()[classname].save()
            return
        elif len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all().keys():
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        else:
            print("** value missing **")
            return

    def do_count(self, s):
        """Retrieve the number of instances of a class."""
        if len(s) == 0:
            print("** class name missing **")
        elif s not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for key, value in storage.all().items():
                if s in key:
                    count += 1
            print(count)

    def default(self, s):
        """Accept arguments in <class name>.all() format."""
        args = s.split(".")

        if len(args) == 1:
            print(f"** Invalid syntax: {s}")
            return
        args1 = args[1].split("(")
        if args1[0] == "all":
            HBNBCommand.do_all(self, args[0])
        elif args1[0] == "count":
            HBNBCommand.do_count(self, args[0])
        elif args1[0] == "show":
            arg_id = args1[1]
            arg_id = arg_id.split(")")
            arg_id = arg_id[0].strip('"')
            argument = args[0] + " " + arg_id
            HBNBCommand.do_show(self, argument)
        elif args1[0] == "destroy":
            arg_id = args1[1]
            arg_id = arg_id.split(")")
            arg_id = arg_id[0].strip('"')
            argument = args[0] + " " + arg_id
            HBNBCommand.do_destroy(self, argument)
        elif args1[0] == "update":
            mul_args = args1[1].split(",", 1)
            arg_id = mul_args[0].strip("'").strip('"')
            arg_dict_str = mul_args[1].strip(')').strip()

            try:
                arg_dict = eval(arg_dict_str)
                if isinstance(arg_dict, dict):
                    for key, value in arg_dict.items():
                        argument = args[0] + " " + arg_id + " " + key +\
                                   " " + repr(value)
                        HBNBCommand.do_update(self, argument)
                else:
                    mul_args = args1[1].split(",")
                    arg_id = mul_args[0]
                    arg_id = arg_id.strip('"')
                    arg_id = arg_id.strip("'")
                    arg_name = mul_args[1]
                    arg_name = arg_name.strip(',')
                    arg_name = arg_name.strip(" ")
                    arg_name = arg_name.strip("'")
                    arg_name = arg_name.strip('"')
                    arg_val = mul_args[2]
                    arg_val = arg_val.strip(" ")
                    arg_val = arg_val.strip(")")
                    argument = args[0] + " " + arg_id + " " + arg_name +\
                        " " + arg_val
                    HBNBCommand.do_update(self, argument)
            except (SyntaxError, NameError, IndexError):
                print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
