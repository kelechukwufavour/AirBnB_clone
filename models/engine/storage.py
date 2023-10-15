#!/usr/bin/python3
'''AirBnB clone project File Storage'''

import json
from models.base_model import BaseModel

class FileStorage:
    '''
    This is a storage engine for the current AirBnB project
    '''
    __file_path = 'file.json'
    __objects = {}
    class_dictn = {"BaseModel": BaseModel}

    def all(self):
        '''Return dictionary of <class>.<id> : object instance'''
        return self.__objects

    def new(self, obj):
        '''Set new object to existing dictionary of instances.'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''Save/serialise obj dictionaries to json file'''
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        '''Load/deserialise obj back to instance, if it exists.'''
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
