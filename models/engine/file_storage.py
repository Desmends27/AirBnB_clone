#!/usr/bin/python3
""" Serializes instances to a json file """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class attributes:
    __file_path: (string): path to the json file
    __objects: dictionary- empty( will store objects
    methods:
    all: returns the dictionary __objects
    new: sets in __objects the obj with key
    save: serializes __objects to json file path
    reload: deserializes the json file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Retursn the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key obj class name.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """ Deserialzes the hson file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as fp:
                objs = json.load(fp)
            for key, value in objs.items():
                name = key.split('.')[0]
                class_ = eval(name)
                self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
