#!/usr/bin/python3

"""
This class contains optional State details that can be supplied
in addition to the baseclass i.e BaseModel class attributes. Also, it
inherit all its parent (all BaseModel) methods.

"""

from models.base_model import BaseModel


class State(BaseModel):
    """This class contains all the optional State details to be supplied

    Attributes:
        Fields:
            name:string - The name of the state
    """
    name = ""
