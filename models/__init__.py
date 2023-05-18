#!/usr/bin/python3

"""
This module creates a unique FileStorage instance for our application.
Using the Method "reload", it deserializes the JSON file i.e it converts
the string dictionary of the classs in json file back to and actual dictionary.
It then convert the dictionary back to an instance, map
<Class.id> to the <instance> and save all in storage object (dict or {}).
This happens each time module model is imported, just to ensure we have
updated instances to work with.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
