#!/usr/bin/python3

"""
This class contains optional user details to be supplied
in addition to the baseclass i.e BaseModel class attributes. Also, it
inherit all its parent (all BaseModel) methods.

"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class contains all the optional user details to be supplied

    Attributes:
        Fields:
            email:string - The user email
            password:string - The user password
            first_name:string - The user first name
            last_name:string - The user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
