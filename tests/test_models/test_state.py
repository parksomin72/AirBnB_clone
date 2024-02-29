#!/usr/bin/python3
"""Module for testing the State class"""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """Test case for the State class"""

    def __init__(self, *args, **kwargs):
        """Initializes TestState"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """Test if name is of type string"""
        new = self.value()
        self.assertIsInstance(new.name, str)
