#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first nane of the user.
        last_name (str): The last name if the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
