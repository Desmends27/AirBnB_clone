#!/usr/bin/python3
""" Base model defines all common attributes/methos for other classess"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
        attributes:
        id: string id of instance created
        create_at: a datetime(assign current datetime)
        updated_at: a datetime(assign current datatime, it will be
                    updated every time you change your object
        methods:
        __init__: initalizer
        __str__: prints: [<class name>] (<self.id>) <self.__dict__>
        public instance methods:
        save: updates the public instance attribute updated_at
        to_dict: returns a dictionary containing all keys/values
    """
    def __init__(self):
        """ Initialiazes the object """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        """ Prints the string representation of an object """
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values """
        dictionary = self.__dict__.copy()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        created = self.created_at.strftime(time_format)
        updated = self.updated_at.strftime(time_format)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["__created_at"] = created
        dictionary["updated_at"] = updated
        return dictionary
