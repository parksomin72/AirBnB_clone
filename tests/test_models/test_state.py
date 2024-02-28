import unittest
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
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-01T00:00:00'
        }
        state = State(**state_dict)
        self.assertEqual(state.id, '789')
        self.assertEqual(state.name, 'Test State')
        self.assertEqual(str(state.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(state.updated_at), '2022-01-01 00:00:00')

if __name__ == '__main__':
    unittest.main()
