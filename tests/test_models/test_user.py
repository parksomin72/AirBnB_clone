#!/usr/bin/python3
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

class User(BaseModel):
    """User class for AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize the User."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        
        # Check if 'created_at' and 'updated_at' are provided as strings
        if 'created_at' in kwargs and isinstance(kwargs['created_at'], str):
            self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S')
        if 'updated_at' in kwargs and isinstance(kwargs['updated_at'], str):
            self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S')

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        """Test user creation."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test setting and getting attributes."""
        user = User()
        user.username = "parksomin72"
        user.email = "fatimazahraealawi@gmail.com"
        self.assertEqual(user.username, "parksomin72")
        self.assertEqual(user.email, "fatimazahraealawi@gmail.com")

    def test_to_dict(self):
        """Test conversion to dictionary."""
        user = User(username="parksomin72", email="fatimazahraealawi@gmail.com")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict.get("email"), "fatimazahraealawi@gmail.com")

    def test_from_dict(self):
        """Test creation from dictionary."""
        user_dict = {
                'id': '123',
                'username': 'parksomin72',
                'email': 'fatimazahraealawi@gmail.com',
                'created_at': datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'),
                'updated_at': datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
                }
        user = User(**user_dict)
        self.assertEqual(user.id, '123')
        self.assertEqual(user.username, 'parksomin72')
        self.assertEqual(user.email, 'fatimazahraealawi@gmail.com')
        self.assertEqual(user.created_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(user.updated_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    unittest.main()
