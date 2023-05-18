#!/usr/bin/python3

"""
This class contains optional City details to be supplied
in addition to the baseclass i.e BaseModel class attributes. Also, it
inherit all its parent (all BaseModel) methods.

"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class contains all the optional City details to be supplied

    Attributes:
        Fields:
            state_id:string - The State.id
            name:string - The City name
    """
    state_id = ""
    name = ""
