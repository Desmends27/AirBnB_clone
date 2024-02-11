#!/usr/bin/python3
""" A user class that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ attributes:
    email: empty string
    password: string
    first_name: empty string
    last_name: empty String
    """
    empty = ""
    password = ""
    first_name = ""
    last_name = ""
