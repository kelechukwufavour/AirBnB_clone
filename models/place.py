#!/usr/bin/python3
'''
Place is a subclass of BaseModel class
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''
    A subclass of BaseModel class
    Public class attributes:
        city_id: string - (str) it will be the City.id
        user_id: string - (str) it will be the User.id
        name: string - (str)
        description: (str)
        number_rooms: (int) - 0
        number_bathrooms: (int) - 0
        max_guest: (int) - 0
        price_by_night: (int) - 0
        latitude: float - (float) 0.0
        longitude: float - (float) 0.0
        amenity_ids: (list of string) it will be the list of Amenity.id
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
