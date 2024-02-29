#!/usr/bin/python3
import unittest
from datetime import datetime
from models.state import State

class TestState(unittest.TestCase):
    def test_state_creation(self):
        """Test state creation."""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_attributes(self):
        """Test setting and getting attributes."""
        state = State()
        state.name = "Test State"
        self.assertEqual(state.name, "Test State")

    def test_to_dict(self):
        """Test conversion to dictionary."""
        state = State(name="Test State")
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['name'], "Test State")

    def test_from_dict(self):
        """Test creation from dictionary."""
        state_dict = {
            'id': '789',
            'name': 'Test State',
            'created_at': datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'),
            'updated_at': datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
        }
        state = State(**state_dict)
        self.assertEqual(state.id, '789')
        self.assertEqual(state.name, 'Test State')
        self.assertEqual(state.created_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))
        self.assertEqual(state.updated_at, datetime.strptime('2022-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    unittest.main()
