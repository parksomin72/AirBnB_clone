#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_str_representation(self):
        """Test string representation."""
        model = BaseModel(id='49ef9b07-ab18-4a63-a4f3-fb5d71b8109f', name='Test Model')
        self.assertEqual(str(model), f"[BaseModel] ({model.id}) {model.__dict__}")

if __name__ == '__main__':
    unittest.main()
