#!/usr/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_from_dict(self):
        """Test creation from dictionary."""
        amenity_dict = {
            'id': '123',
            'name': 'test amenity',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00'
        }
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.name, 'test amenity')
        self.assertEqual(amenity.created_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(amenity.updated_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    unittest.main()
