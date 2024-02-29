#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from models.user import User

class TestBaseModel(unittest.TestCase):
    def test_str_representation(self):
        """Test string representation."""
        model = BaseModel(id='49ef9b07-ab18-4a63-a4f3-fb5d71b8109f', name='Test Model')
        self.assertEqual(str(model), f"[BaseModel] ({model.id}) {model.__dict__}")

class TestPlace(unittest.TestCase):
    def test_to_dict(self):
    """Test conversion to dictionary."""
    place = Place(name="Test Place")
    place_dict = place.to_dict()
    self.assertIsInstance(place_dict, dict)
    self.assertEqual(place_dict.get('name'), "Test Place")

class TestUser(unittest.TestCase):
    def test_to_dict(self):
        """Test conversion to dictionary."""
        user = User(username="parksomin72", email="fatimazahraealawi@gmail.com")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict.get('email'), 'fatimazahraealawi@gmail.com')

if __name__ == '__main__':
    unittest.main()
