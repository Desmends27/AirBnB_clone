#!/usr/bin/python3
""" Amentity class, inherits from BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    attrs:
    name: name of amenity
    """
    name = ""
