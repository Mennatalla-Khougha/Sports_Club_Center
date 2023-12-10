#!/usr/bin/python3
"""This program is for the console"""
import cmd
import re
import json
from models.BaseModel import BaseModel
from models.player import Player
from models.tournament import Tournament
from models.sport import Sport
from models.record import Record
from models import storage
import shlex
import sqlalchemy
from PIL import Image


classes = ["BaseModel", "Player", "Tournament", "Sport", "Record"]


def error(args):
    """check if the command is wrong"""
    if not args:
        print("** class name missing **")
        return True

    if args[0] not in classes:
        print("** class doesn't exist **")
        return True

    if len(args) < 2:
        print("** instance id missing **")
        return True

    key = f"{args[0]}.{args[1]}"
    if key not in storage.all().keys():
        print("** no instance found **")
        return True
    return False


class ConsoleCommand(cmd.Cmd):
    """Console class"""
    prompt = ">>> "

    def do_quit(self, arg):
        """
        Exit the program
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with EOF
        Usage: EOF (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """Do nothing upon reciving an empty line"""
        return

    def do_help(self, arg):
        """
        Show help information
        Usage: help <command>
        """
        super().do_help(arg)

    def do_create(self, arg):
        """
        Create a new instance of a given class.
        Usage: create <class name> {keys: values}
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ', 1)
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** missing attrebutes **")
            return
        try:
            data = json.loads(args[1])
            obj = eval(args[0])(**data)
            obj.save()
        except json.JSONDecodeError:
            print("** Invalid JSON format. **")
            return
        except sqlalchemy.exc.OperationalError:
            print("** some attrebute(s) are missing or invalid **")
            storage.rollback()
            return
        if isinstance(obj, Player) or isinstance(obj, Tournament):
            photo = input("Enter the path of the photo or (n) for no photo: ")
            if photo != "n":
                try:
                    img = Image.open(photo)
                    new_path = "website/static/images/"
                    if isinstance(obj, Player):
                        new_path += f"personal/{obj.id}.png"
                    else:
                        new_path += f"tournaments/{obj.id}.png"
                    img.save(new_path, format='PNG', compress_level=0)
                except IOError as e:
                    print(e)
        print(obj.id)

    def do_show(self, arg):
        """
        Print string representation of an object.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if error(args):
            return
        key = f"{args[0]}.{args[1]}"
        print(storage.all()[key].to_dict())

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if error(args):
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all()[key]
        obj.delete()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        Usage: all <class name> or all
        """
        lst = []
        if not arg:
            for value in storage.all().values():
                lst.append(value.to_dict())
        elif arg not in classes:
            print("** class doesn't exist **")
            return
        else:
            for key, value in storage.all().items():
                if arg in key:
                    lst.append(value.to_dict())
        print(lst)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        Usage: update <class name> <id> {keys: values}
        """
        args = arg.split(' ', 2)
        if error(args):
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attributes are missing **")
            return

        obj = storage.all()[key]

        try:
            data = json.loads(args[2])
        except json.JSONDecodeError:
            print("** Invalid JSON format. **")
            return
        for key, value in data.items():
            if key == "photo" and args[0] in ("Player", "Tournament"):
                try:
                    img = Image.open(value)
                    new_path = "website/static/images/"
                    if args[0] == "Player":
                        new_path = f"personal/{obj.id}.png"
                    else:
                        new_path = f"tournaments/{obj.id}.png"
                    img.save(new_path, format='PNG', compress_level=0)
                except IOError as e:
                    print(e)
            else:
                setattr(obj, key, value)
        obj.save()

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        methods = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        args = re.split(r'(?<!\d)\.(?!\d)', arg)
        if len(args) != 2:
            print(f"*** Unknown syntax: {arg}")
            return
        command = args[1].split("(")
        if len(args[0]) == 0 and command[0] in methods.keys():
            print("** class name missing **")
            return
        if len(command) != 2 or command[0] not in methods.keys():
            print(f"*** Unknown syntax: {arg}")
        elif command[1][-1] != ")":
            print(f"*** Unknown syntax: {arg}")
        elif args[0] not in classes and command[0] != "count":
            print("** class doesn't exist **")
        else:
            command[1] = command[1][:-1]
            mydict = re.search(r"\{(.*?)\}", command[1])
            if mydict is None:
                split_parts = shlex.split(command[1])
            else:
                split_parts = shlex.split(command[1][:mydict.span()[0]])
            split_parts = [i.strip(",") for i in split_parts]
            split_parts = [f'"{s}"' if ' ' in s else s for s in split_parts]
            split_parts = ' '.join(split_parts)
            if split_parts:
                para = f"{args[0]} {split_parts}"
            else:
                para = args[0]
            if mydict is None:
                methods[command[0]](para)
            else:
                input_str = command[1][mydict.span()[0]:mydict.span()[1]]
                input_str = input_str.replace("'", '"')
                myargs = json.loads(input_str)
                for key, value in myargs.items():
                    # if type(value) == str and ' ' in value:
                    if isinstance(value, str) and ' ' in value:
                        value = f'"{value}"'
                    methods[command[0]](f"{para} {key} {value}")

    def do_count(self, arg):
        """
        Prints number of instances of a given class.
        Usage: count <class name>
        """
        print(storage.count(arg))

    def do_append(self, arg):
        """
        Add player to a tournment.
        Usage: append <player id> <tournment id>
        """
        if not arg:
            print("** player id missing **")
            return
        args = arg.split()
        player = storage.get("Player", args[0])
        if not player:
            print("** no Player instance found **")

        if len(args) < 2:
            print("** id missing **")
            return

        obj = storage.get("Tournment", args[1])
        if not obj:
            print(f"** no Tournment instance found **")
            return

        player.join_tournament(obj)
        storage.save()


if __name__ == '__main__':
    ConsoleCommand().cmdloop()
