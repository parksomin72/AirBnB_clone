# tests/test_example.py

import unittest

class ExampleTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(3 - 1, 2)

if __name__ == '__main__':
    unittest.main()
