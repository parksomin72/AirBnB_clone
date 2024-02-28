#!/usr/bin/python3
"""BaseModel module for the AirBnB project."""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class for AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Return a string representation of the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    print(my_model)
