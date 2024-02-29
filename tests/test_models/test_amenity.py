#!/usr/bin/python3
"""Module for testing the Amenity class"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class TestAmenity(test_basemodel):
    """Test case for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes TestAmenity"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_type(self):
        """Test if name is of type string"""
        new = self.value()
        self.assertIsInstance(new.name, str)
