#!/usr/bin/python3
"""Module for testing the Place class"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(test_basemodel):
    """Test case for the Place class"""

    def __init__(self, *args, **kwargs):
        """Initializes TestPlace"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id_type(self):
        """Test if city_id is of type string"""
        new = self.value()
        self.assertIsInstance(new.city_id, str)

    def test_user_id_type(self):
        """Test if user_id is of type string"""
        new = self.value()
        self.assertIsInstance(new.user_id, str)

    def test_name_type(self):
        """Test if name is of type string"""
        new = self.value()
        self.assertIsInstance(new.name, str)

    def test_description_type(self):
        """Test if description is of type string"""
        new = self.value()
        self.assertIsInstance(new.description, str)

    def test_number_rooms_type(self):
        """Test if number_rooms is of type int"""
        new = self.value()
        self.assertIsInstance(new.number_rooms, int)

    def test_number_bathrooms_type(self):
        """Test if number_bathrooms is of type int"""
        new = self.value()
        self.assertIsInstance(new.number_bathrooms, int)

    def test_max_guest_type(self):
        """Test if max_guest is of type int"""
        new = self.value()
        self.assertIsInstance(new.max_guest, int)

    def test_price_by_night_type(self):
        """Test if price_by_night is of type int"""
        new = self.value()
        self.assertIsInstance(new.price_by_night, int)

    def test_latitude_type(self):
        """Test if latitude is of type float"""
        new = self.value()
        self.assertIsInstance(new.latitude, float)

    def test_longitude_type(self):
        """Test if longitude is of type float"""
        new = self.value()
        self.assertIsInstance(new.longitude, float)

    def test_amenity_ids_type(self):
        """Test if amenity_ids is of type list"""
        new = self.value()
        self.assertIsInstance(new.amenity_ids, list)
