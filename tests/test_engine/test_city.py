#!/usr/bin/python3
"""Unit tests for City class."""

from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """Test cases for City class."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_type(self):
        """Test type of City state_id attribute."""
        new = self.value()
        self.assertIsInstance(new.state_id, str)

    def test_name_type(self):
        """Test type of City name attribute."""
        new = self.value()
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
