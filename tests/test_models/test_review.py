#!/usr/bin/python3
import unittest
from datetime import datetime
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_creation(self):
        """Test review creation."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        """Test setting and getting attributes."""
        review = Review()
        review.text = "Great experience!"
        review.user_id = "123"
        review.place_id = "456"
        self.assertEqual(review.text, "Great experience!")
        self.assertEqual(review.user_id, "123")
        self.assertEqual(review.place_id, "456")

    def test_to_dict(self):
        """Test conversion to dictionary."""
        review = Review(text="Great experience!", user_id="123", place_id="456")
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['text'], "Great experience!")
        self.assertEqual(review_dict['user_id'], "123")
        self.assertEqual(review_dict['place_id'], "456")

    def test_from_dict(self):
        """Test creation from dictionary."""
        review_dict = {
            'id': '789',
            'text': 'Great experience!',
            'user_id': '123',
            'place_id': '456',
            'created_at': datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'updated_at': datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
        }
        review = Review(**review_dict)
        self.assertEqual(review.id, '789')
        self.assertEqual(review.text, 'Great experience!')
        self.assertEqual(review.user_id, '123')
        self.assertEqual(review.place_id, '456')
        self.assertEqual(review.created_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(review.updated_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    unittest.main()
