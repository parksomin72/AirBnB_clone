#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        """Test setting and getting attributes."""
        model = BaseModel()
        model.name = "Test Model"
        self.assertEqual(model.name, "Test Model")

    def test_to_dict(self):
        """Test conversion to dictionary."""
        model = BaseModel()
        model.name = "Test Model"
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['name'], "Test Model")

    def test_from_dict(self):
        """Test creation from dictionary."""
        model_dict = {
            'id': '123',
            'name': 'Test Model',
            'created_at': datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'updated_at': datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
        }
        model = BaseModel(**model_dict)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(model.created_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(model.updated_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))

    def test_str_representation(self):
    """Test string representation."""
    model = BaseModel()
    model.id = 'test_id'
    model.name = "Test Model"
    self.assertEqual(str(model), "[BaseModel] ({} {})".format(model.id, model.__dict__))

if __name__ == '__main__':
    unittest.main()
