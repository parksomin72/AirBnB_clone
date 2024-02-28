import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        """Test amenity creation."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        """Test setting and getting attributes."""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_to_dict(self):
        """Test conversion to dictionary."""
        amenity = Amenity(name="Wifi")
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['name'], "Wifi")

    def test_from_dict(self):
        """Test creation from dictionary."""
        amenity_dict = {
            'id': '789',
            'name': 'Wifi',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00'
        }
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.id, '789')
        self.assertEqual(amenity.name, 'Wifi')
        self.assertEqual(str(amenity.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(amenity.updated_at), '2022-01-01 00:00:00')

if __name__ == '__main__':
    unittest.main()
