#!/usr/bin/python3
""" Base model defines all common attributes/methos for other classess"""
from uuid import uuid4
from datetime import datetime
import models


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
    def __init__(self, *args, **kwargs):
        """ Initialiazes the object """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    time_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    time_format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ Prints the string representation of an object """
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dictionary = self.__dict__.copy()
        created = self.created_at.strftime(time_format)
        updated = self.updated_at.strftime(time_format)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = created
        dictionary["updated_at"] = updated
        return dictionary
