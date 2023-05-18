#!/usr/bin/python3

"""
This class contains optional Review details to be supplied
in addition to the baseclass i.e BaseModel class attributes. Also, it
inherit all its parent (all BaseModel) methods.

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class contains all the optional Review details to be supplied

    Attributes:
        Fields:
            place_id:string - The Place.id
            user_id:string - The User.id
            text:string - Review comments
    """
    place_id = ""
    user_id = ""
    text = ""
