#!/usr/bin/python3
""" City model that inherits from baseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """
    attrs:
    state_id: id of state, empty string
    name: empty string, name of city
    """
    name = ""
