#!/usr/bin/python3
'''Defines the FileStorage class.'''
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class FileStorage:
    '''Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Return the dictionary __objects.'''
        return FileStorage.__objects

    def new(self, obj):
        '''Set in __objects obj with key <obj_class_name>.id'''
        o_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(o_name, obj.id)] = obj

    def save(self):
        '''Serialize __objects to the JSON file __file_path.'''
        o_dict = FileStorage.__objects
        objdict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        '''Deserialize the JSON file __file_path to __objects, if it exists.'''
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
