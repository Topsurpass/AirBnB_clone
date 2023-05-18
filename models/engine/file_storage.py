#!/usr/bin/python3

"""
This module serializes instances to JSON file and deserializes JSON file
back to instances.

Here is the flow of serialization-deserialization:
    instance -> dictionary -> string -> dictionary -> instance

"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """This class serializes instances to JSON format and deseriazes
    it back to instances

    Attribute:
            Fields:
                __file_path:string - path to the JSON file(ex: file.json)
                __objects:dictionary - store all instances by key classname.id
                    (ex: BaseModel.1212121212)

            Methods:
                all(self): Returns the dictionary __objects
                new(self, obj): Map <instance class>.<id> to <instance>
                    and Sets in __objects dictionary
                save(self): Serializes __objects to the JSON file path
                    (path: __file_path)
                reload(self): If JSON file (__file_path) exist, deserializes
                    the JSON file to __objects

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Add new instance to __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes all instances in __object dictionary to JSON"""
        new_obj = {}
        for key in self.__objects.keys():
            new_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_obj, f)

    def reload(self):
        """Deserializes JSON file to instance and put it in __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                new_dict = json.load(f)
            for val in new_dict.values():
                """create an instance of a particular class based on the
                value of __class__ in a dictionary"""
                cls = val["__class__"]
                """recreat instance from the dictionary"""
                self.new(eval(cls)(**val))
        except FileNotFoundError:
            pass
