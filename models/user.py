#!/usr/bin/python3
"""User module for the AirBnB project."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize the User."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")


if __name__ == "__main__":
    my_user = User()
    print(my_user)
