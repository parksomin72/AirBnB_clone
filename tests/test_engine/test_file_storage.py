import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()

    def test_all(self):
        """Test retrieval of all objects."""
        # Add some objects to storage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Test if all objects are retrieved
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(obj1.__class__.__name__ + '.' + obj1.id, all_objs)
        self.assertIn(obj2.__class__.__name__ + '.' + obj2.id, all_objs)

    def test_new(self):
        """Test addition of a new object."""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, all_objs)

    def test_save(self):
        """Test saving objects to file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Check if the file has been created
        with open(self.storage._FileStorage__file_path, 'r') as file:
            content = file.read()
            self.assertIn(obj.__class__.__name__ + '.' + obj.id, content)

    def test_reload(self):
        """Test reloading objects from file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        
        # Clear storage
        del self.storage._FileStorage__objects

        # Reload and check if the object exists
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, all_objs)

if __name__ == '__main__':
    unittest.main()
