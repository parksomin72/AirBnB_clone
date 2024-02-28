import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_creation(self):
        """Test city creation."""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        """Test setting and getting attributes."""
        city = City()
        city.name = "Test City"
        city.state_id = "123"
        self.assertEqual(city.name, "Test City")
        self.assertEqual(city.state_id, "123")

    def test_to_dict(self):
        """Test conversion to dictionary."""
        city = City(name="Test City", state_id="123")
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['name'], "Test City")
        self.assertEqual(city_dict['state_id'], "123")

    def test_from_dict(self):
        """Test creation from dictionary."""
        city_dict = {
            'id': '789',
            'name': 'Test City',
            'state_id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00'
        }
        city = City(**city_dict)
        self.assertEqual(city.id, '789')
        self.assertEqual(city.name, 'Test City')
        self.assertEqual(city.state_id, '123')
        self.assertEqual(str(city.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(city.updated_at), '2022-01-01 00:00:00')

if __name__ == '__main__':
    unittest.main()
