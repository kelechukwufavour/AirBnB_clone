#!/usr/bin/python3
import uuid
from datetime import datetime
import models

'''
Main parent class to all classes in the Airbnb clone project
'''


class BaseModel():
    '''
    Parent class to all classes in the Airbnb clone project
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialise attributes: uuid4, dates when class was created/updated
        '''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        Return class name, id, and the dictionary
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Instance method to update current datetime,
        invoke save and save to serializes file
        '''
        self.updated_at = datetime.now()
        models.storage(self)

    def to_dict(self):
        '''
        Return dictionary of basemodel with string formats of times
        '''
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
