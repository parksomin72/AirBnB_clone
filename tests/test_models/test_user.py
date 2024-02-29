#!/usr/bin/python3
"""Unit tests for User class."""

from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """Test cases for User class."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_type(self):
        """Test type of User first_name attribute."""
        new = self.value()
        self.assertIsInstance(new.first_name, str)

    def test_last_name_type(self):
        """Test type of User last_name attribute."""
        new = self.value()
        self.assertIsInstance(new.last_name, str)

    def test_email_type(self):
        """Test type of User email attribute."""
        new = self.value()
        self.assertIsInstance(new.email, str)

    def test_password_type(self):
        """Test type of User password attribute."""
        new = self.value()
        self.assertIsInstance(new.password, str)


if __name__ == '__main__':
    unittest.main()
