#!/usr/bin/python3
"""Unit tests for Review class."""

from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Test cases for Review class."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_type(self):
        """Test type of Review place_id attribute."""
        new = self.value()
        self.assertIsInstance(new.place_id, str)

    def test_user_id_type(self):
        """Test type of Review user_id attribute."""
        new = self.value()
        self.assertIsInstance(new.user_id, str)

    def test_text_type(self):
        """Test type of Review text attribute."""
        new = self.value()
        self.assertIsInstance(new.text, str)


if __name__ == '__main__':
    unittest.main()
