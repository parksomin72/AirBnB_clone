#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_from_dict(self):
        """Test creation from dictionary."""
        amenity_dict = {
            'id': '123456',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00',
            'name': 'Test Amenity'
        }
        amenity = Amenity(**amenity_dict)
        
        self.assertEqual(amenity.id, '123456')
        self.assertEqual(amenity.created_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(amenity.updated_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(amenity.name, 'Test Amenity')


if __name__ == '__main__':
    unittest.main()
