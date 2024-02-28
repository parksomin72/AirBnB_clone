import unittest
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
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00'
        }
        model = BaseModel(**model_dict)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(str(model.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(model.updated_at), '2022-01-01 00:00:00')

    def test_str_representation(self):
        """Test string representation."""
        model = BaseModel()
        model.name = "Test Model"
        self.assertEqual(str(model), "[BaseModel] ({} {})".format(model.id, model.__dict__))

if __name__ == '__main__':
    unittest.main()
