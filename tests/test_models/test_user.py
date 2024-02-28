import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        """Test user creation."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test setting and getting attributes."""
        user = User()
        user.username = "testuser"
        user.email = "testuser@example.com"
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")

    def test_to_dict(self):
        """Test conversion to dictionary."""
        user = User(username="testuser", email="testuser@example.com")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['username'], "testuser")
        self.assertEqual(user_dict['email'], "testuser@example.com")

    def test_from_dict(self):
        """Test creation from dictionary."""
        user_dict = {
            'id': '123',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00'
        }
        user = User(**user_dict)
        self.assertEqual(user.id, '123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(str(user.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(user.updated_at), '2022-01-01 00:00:00')

if __name__ == '__main__':
    unittest.main()
