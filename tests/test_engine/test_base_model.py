#!/usr/bin/python3
"""Unit tests for BaseModel class."""

import unittest
import datetime
import json
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Set up method to prepare test environment."""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up method to reset test environment."""
        del self.model
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default_constructor(self):
        """Test default constructor."""
        self.assertIsInstance(self.model, BaseModel)

    def test_save(self):
        """Test saving object to JSON file."""
        self.model.save()
        with open('file.json', 'r') as f:
            data = json.load(f)
            key = "BaseModel." + self.model.id
            self.assertEqual(data[key], self.model.to_dict())

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_to_dict(self):
        """Test conversion of BaseModel instance to dictionary."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_id_type(self):
        """Test type of BaseModel ID."""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_type(self):
        """Test type of BaseModel created_at attribute."""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """Test type of BaseModel updated_at attribute."""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_created_updated_not_equal(self):
        """Test that created_at and updated_at are not equal."""
        self.assertNotEqual(self.model.created_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()
