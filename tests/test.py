#!/usr/bin/python3
"""Test module for the AirBnB project."""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """TestBaseModel class to test the BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.my_model = BaseModel()
        self.additional_data = {"key": "value"}

    def tearDown(self):
        """Tear down test environment."""
        # Any teardown code you need after each test case
        del self.my_model
        # Additional teardown code

    def test_create_instance(self):
        """Test creating an instance of BaseModel."""
        # Access the setup data
        initial_data = self.additional_data
        self.assertIsInstance(self.my_model, BaseModel)

    def test_attributes(self):
        """Test attributes of BaseModel."""
        # Access the setup data
        initial_data = self.additional_data
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
