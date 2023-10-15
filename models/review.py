#!/usr/bin/python3
'''
Review is a subclass of BaseModel class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    A subclass of BaseModel class
    Public class attributes:
        place_id: string - (str) it will be the Place.id
        user_id: string - (str) it will be the User.id
        text: string - (str)
    '''
    place_id = ""
    user_id = ""
    text = ""
