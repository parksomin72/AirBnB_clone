#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Class to serialize and deserialize instances to JSON file and vice versa."""
    
    def __init__(self):
        """Initializes FileStorage instance."""
        ...
        self.__objects = {}
    
    __classes = {
        'BaseModel': BaseModel,
        'User': User
    }

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    ...
    
    def deserialize(self):
        """Deserializes the JSON file to create instances."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                data = json.load(f)
                for k, v in data.items():
                    cls_name = v['__class__']
                    if cls_name in self.__classes:
                        self.__objects[k] = self.__classes[cls_name](**v)
