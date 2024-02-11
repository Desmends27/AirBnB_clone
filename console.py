#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage


classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place,
           "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter for AirBnB """
    prompt = '(hbnb) '

    def emptyline(self):
        """ Do nothing if an empty is entered """
        pass

    @classmethod
    def line_check(self, arg):
        """ Checks for emptyline or class existing """
        if len(arg) == 0:
            print('** class name missing **')
            return False
        elif arg not in classes:
            print("** class doesn't exist **")
            return False
        return True

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Quit the program also\n'
        return True

    def do_create(self, arg):
        """ Creates a new instance of BaseModel and saves it """
        if self.line_check(arg):
            cls = classes[arg]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ Prints the string representation base on the class name and id """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            cls = arg.split(' ')[0]
            if self.line_check(cls):
                if len(arg.split(" ")) == 1:
                    print('** instance id missing **')
                else:
                    id_ = arg.split(' ')[1]
                    key = f"{cls}.{id_}"
                    try:
                        print(storage._FileStorage__objects[key])
                    except KeyError:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an object from storage engine """
        cls = arg.split(' ')[0]
        dictobj = storage.all()
        if self.line_check(cls):
            if len(arg.split(" ")) == 1:
                print('** instance id missing **')
            else:
                try:
                    id_ = arg.split(" ")[1]
                    key = f"{cls}.{id_}"
                    del dictobj[key]
                    storage.save()
                except KeyError:
                    print('** no instance found **')

    def do_all(self, arg):
        """ Prints all string representaton of all instances """

        all_objs = storage.all()
        str_repr = ""
        if len(arg) == 0:
            for key, value in all_objs.items():
                str_repr += str(value)
        else:
            if arg not in classes:
                print("** class doesn't exist **")
            else:
                for key, value in all_objs.items():
                    cls = key.split(".")[0]
                    if cls == arg:
                        str_repr += str(value)
                print(str_repr)

    def do_update(self, arg):
        """ Updates an insance based on the class name and id """
        args = arg.split(" ")
        all_objs = storage.all()
        cls = args[0]
        id_ = args[1]
        attr_name = args[2]
        attr_value = args[3]
        if len(cls) == 0:
            print("** class name missing **")
        elif cls not in classes:
            print("** class doesn't exist **")
        elif len(id_) == 0:
            print("** instance id missing **")
        else:
            try:
                key = f"{cls}.{id_}"
                obj = all_objs[key]
                if len(attr_name) == 0:
                    print("** attribute name missing **")
                elif len(attr_value) == 0:
                    print(" ** value missing ***")
                else:
                    setattr(obj, attr_name, attr_value)
            except KeyError:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
