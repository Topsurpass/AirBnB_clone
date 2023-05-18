#!/usr/bin/python3

"""
This class contains optional Place details to be supplied
in addition to the baseclass i.e BaseModel class attributes. Also, it
inherit all its parent (all BaseModel) methods.

"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This class contains all the optional Place details to be supplied

    Attributes:
        Fields:
            city_id:string - The City.id
            user_id:string - The User.id
            name:string - The name of the place
            description:string - The desription of the place
            number_rooms:integer - The number of rooms in the place
            number_bathrooms:integer - The number of bathrooms in the place
            max_guest:integer The maximum number of guest that the place can
                occupy
            price_by_night:integer - Price per night
            latitude:float - The latitude of the place
            longitude:float - The longitude of the place
            amenity_ids:list of string - List of Amenity.id

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
