#!/usr/bin/python3
"""Unit tests for City class."""

import unittest
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """Test cases for City class."""

    def setUp(self):
        """Set up method to prepare test environment."""
        self.model = City()

    def tearDown(self):
        """Clean up method to reset test environment."""
        del self.model

    def test_state_id(self):
        """Test state_id attribute."""
        self.assertEqual(type(self.model.state_id), str)

    def test_name(self):
        """Test name attribute."""
        self.assertEqual(type(self.model.name), str)


if __name__ == '__main__':
    unittest.main()
