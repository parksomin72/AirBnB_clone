#!/usr/bin/python3
"""FileStorage module for the AirBnB project."""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class for AirBnB project."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserialize the JSON file (path: __file_path) to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                load_dict = json.load(file)
                for key, value in load_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
    print(storage.all())
