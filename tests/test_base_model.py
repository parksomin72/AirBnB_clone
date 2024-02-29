#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_str_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_output = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_output)

    def test_save_method(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('__class__', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIn('id', my_model_dict)
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertIn('created_at', my_model_dict)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertIn('updated_at', my_model_dict)
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
