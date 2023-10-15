#!/usr/bin/python3
import models
import uuid
from datetime import datetime

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
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
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
        models.storage.save()

    def to_dict(self):
        '''
        Return dictionary of basemodel with string formats of times
        '''
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
