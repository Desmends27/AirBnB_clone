#!/usr/bin/python3
""" Review class, inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ attrs:
    place_id : empty string
    user_idempty string
    text: empty string
    """
    place_id = ""
    user_id = ""
    text = ""
