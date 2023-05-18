#!/usr/bin/python3

"""
This module contains the entry point of the command interpreter
i.e the console. The command interpreter helps to manipulate data
without visual interface, like in a shell. It is perfect for
development and debugging.

"""

import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class contains the entry point of the command interpreter
    Attributes:
        Fields:
            prompt: Customize the command interpreter prompt
        Methods:
            do_quit(self, line): Quit the cosole using "quit" command
            do_EOF(self, line): Quit the console using "CTRL-D" keyboard
            emptyline(self): Disable repitition of last/previous command
            do_create(self, line): Create new instance of specified class
            do_show(self, line): Display instances using class and ID
            do_destroy(self, line): Destroy an instance using it's class and ID
            do_all(self, line): List all instances based on specified class/not
            do_update(self, line): Update an instance by adding more attributes
            through dictionary or by specifying the attribute name value pair
    """
    valid_classes = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Use CTRL-D to quit the command interpreter"""
        print()
        return True

    def emptyline(self):
        """Disable prvious command"""
        pass

    def do_create(self, line):
        """Creates new instance based on specified class"""
        if not line:
            print("** class name missing **")
            return
        commands = line.split()
        if commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        else:
            new_obj = eval(commands[0])()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Print string representation of an instance based on specified class and id"""

        if not line:
            print("** class name missing **")
            return
        commands = line.split()
        if commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(commands) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = "{}.{}".format(commands[0], commands[1])
                if key in storage.all(): 
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
                    return
            except Exception:
                return

    def do_destroy(self, line):
        """Delete an instance from storage based on the class specified and id"""
        if not line:
            print("** class name missing **")
            return
        commands = line.split()
        if commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(commands) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = "{}.{}".format(commands[0], commands[1])
                del storage.all()[key]
                storage.save()
                storage.reload()
            except Exception:
                print("** no instance found **")
                return

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class specified"""
        all_obj = []
        response = "** class doesn't exist **"
        if not line:
            [all_obj.append(str(i)) for i in storage.all().values()]
        else:
            if line not in self.valid_classes:
                print(response)
                return
            else:
                [
                        all_obj.append(str(i)) for i in storage.all().values()
                        if i.__class__.__name__ == line]
        print(all_obj)

    def do_count(self, line):
        """count number of instances present in a specified class"""
        if line not in self.valid_classes:
            print("** class doesn't exist **")
            return
        else:
            num = sum(
                    1 for i in storage.all().values()
                    if i.__class__.__name__ == line)
            print(num)

    def do_update(self, line):
        """Update an instance based on the class specified and id by adding or
        updating attribute and saving in a file"""
        if not line:
            print("** class name missing **")
            return
        """Capture text in curly braces {} or "" and put in a list"""
        pattern = r'({.*?})|(\".*?\")'
        txt_in_braces = re.findall(pattern, line)

        """Replace spaces in the list above with ### and
        join them with the line"""
        for space in txt_in_braces:
            space_str = "".join(space)
            line = line.replace(space_str, space_str.replace(' ', '###'))

        """Split the line using space and replace ### in
        {} and "" back with spaces"""
        commands = [c.replace('###', ' ') for c in line.split()]

        if commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif len(commands) == 2:
            key = "{}.{}".format(commands[0], commands[1].strip('"').strip("'"))
            if key not in storage.all():
                print("** no instance found **")
                return
            else:
                print("** attribute name missing **")
                return
        elif len(commands) == 3:
            if commands[2].startswith('{'):
                if commands[2].endswith('}'):
                    my_dict = eval(commands[2])
                    key = "{}.{}".format(commands[0], commands[1].strip('"').strip("'"))
                    update_obj = storage.all()[key]
                    for k, v in my_dict.items():
                        setattr(update_obj, k, v)
                    update_obj.save()
                else:
                    print("** invalid synthax **")
                    return
            else:
                print("** value missing **")
                return
        elif len(commands) == 4:
            val = commands[3]
            if type(eval(val)) not in (float, int, dict):
                val = str(val).strip('"').strip("'")
            else:
                val = eval(val)
            key = "{}.{}".format(commands[0], commands[1].strip('"').strip("'"))
            if key in storage.all():
                update_obj = storage.all()[key]
                cmd_key = commands[2].strip("'").strip('"')
                setattr(update_obj, cmd_key, val)
                update_obj.save()
            else:
                print("** no instance found **")
                return
        else:
            print("** invalid synthax **")
            return

    def default(self, line):
        """Retrieve all instances of a class using classname.command.
        The command can be all(), count() e.t.c."""
        cmd_arr = line.split(".")
        cls = cmd_arr[0]
        if len(cmd_arr) == 1:
            return
        elif cls == "":
            print("** class name missing **")
            return
        elif cls not in self.valid_classes:
            print("** class doesn't exist **")
            return
        methd = cmd_arr[1]
        try:
            commands = methd.split("(")
            if commands[0] == "all" and commands[1] == ")":
                self.do_all(cls)
            elif commands[0] == "count" and commands[1] == ")":
                self.do_count(cls)
            elif commands[0] == "show" and commands[1].endswith(")"):
                obj_id = str(commands[1]).strip('()"')
                new_line = "{} {}".format(cls, obj_id)
                self.do_show(new_line)
            elif commands[0] == "destroy" and commands[1].endswith(")"):
                obj_id = str(commands[1]).strip('()"')
                new_line = "{} {}".format(cls, obj_id)
                self.do_destroy(new_line)
            elif commands[0] == "update" and commands[1].endswith(")"):
                pattern = r'({.*?})'
                dic = re.findall(pattern, line)
                obj_id = commands[1].split(',')[0][1:-1]
                if not dic:
                    new_line = "{} {}".format(cls, " ".join(commands[1][:-1].split(',')))
                else:
                    new_line = "{} {} {}".format(cls, obj_id.strip('"').strip("'"), dic[0])
                self.do_update(new_line)
            else:
                print("** invalid syntax **")
                return
        except Exception:
                print("** invalid syntax **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
