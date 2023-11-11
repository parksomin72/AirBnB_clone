#!/usr/bin/python3
"""File Storage module"""
import json
from models.base_model import BaseModel

class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                data = json.load(f)
            for key, value in data.items():
                cls_name = value['__class__']
                cls = globals()[cls_name]
                obj = cls(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
