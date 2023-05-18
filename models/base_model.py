#!/usr/bin/python3

"""
    This is the base class for all common attributes/methods for other
    classes for this AIRBNB project.

    The goal of this class is to manage common attributes between all other
    classes.

"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """The base class for all other classes
        Attributes:
            Fields:
                id:string - Unique id for each instance when created
                created_at:datetime - The datetime when an instance was created
                updated_at:datetime - The datetime when an instance created was
                    updated
            Methods:
                __init__(self, *args, **kwargs): Initialize the instance when
                    created either from dictionary key/value pair or otherwise
                __str__(self): Print the instance created in sring format
                save(self): Updates the public instance attribute "updated_at"
                    with the current datetime whenever an instance is modoify
                to_dict(self): Return a dictionary containig all keys/values
                    pairs of an instance

    """
    def __init__(self, *args, **kwargs):
        """Initialize the instances either from dictionary key/value or
        otherwise and save each instance"""
        if kwargs and kwargs != {}:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(kwargs[key])
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(kwargs[key])
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """save each instance created to storage object (i.e dict or {})"""
            models.storage.new(self)

    def __str__(self):
        """Print an instance in string format"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update "updated_at" attribute with current datetime
        and save/write the instance to a file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__

        for key in self.__dict__.keys():
            if isinstance(self.__dict__[key], datetime):
                new_dict[key] = self.__dict__[key].isoformat()
            else:
                new_dict[key] = self.__dict__[key]
        return new_dict
