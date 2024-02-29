#!/usr/bin/python3
"""Unit tests for Amenity class."""

import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """Test cases for Amenity class."""

    def setUp(self):
        """Set up method to prepare test environment."""
        self.model = Amenity()

    def tearDown(self):
        """Clean up method to reset test environment."""
        del self.model

    def test_name(self):
        """Test name attribute."""
        self.assertEqual(type(self.model.name), str)


if __name__ == '__main__':
    unittest.main()
