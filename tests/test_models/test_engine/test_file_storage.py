#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up method to prepare test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up method to reset test environment."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_reload(self):
        """Test reloading objects from file."""
        # Save some data
        obj = BaseModel()
        obj.save()
        # Get the current state of __objects
        current_objects = dict(self.storage._FileStorage__objects)
        # Reload the data
        self.storage.reload()
        # Check if the objects are reloaded correctly
        for key, value in current_objects.items():
            self.assertIn(key, self.storage._FileStorage__objects)
            self.assertEqual(value.__class__.__name__, self.storage._FileStorage__objects[key].__class__.__name__)


if __name__ == '__main__':
    unittest.main()
