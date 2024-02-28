import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        """Test place creation."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        """Test setting and getting attributes."""
        place = Place()
        place.name = "Test Place"
        place.city_id = "123"
        place.user_id = "456"
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")

    def test_to_dict(self):
        """Test conversion to dictionary."""
        place = Place(name="Test Place", city_id="123", user_id="456")
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['name'], "Test Place")
        self.assertEqual(place_dict['city_id'], "123")
        self.assertEqual(place_dict['user_id'], "456")

    def test_from_dict(self):
        """Test creation from dictionary."""
        place_dict = {
            'id': '789',
            'name': 'Test Place',
            'city_id': '123',
            'user_id': '456',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00'
        }
        place = Place(**place_dict)
        self.assertEqual(place.id, '789')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(str(place.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(place.updated_at), '2022-01-01 00:00:00')

if __name__ == '__main__':
    unittest.main()
