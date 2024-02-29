import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertIn("valid UUID", f.getvalue().strip())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertIn(obj_id, f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.assertNotIn(obj_id, f.getvalue())

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertEqual("[]", f.getvalue().strip())

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertEqual("0", f.getvalue().strip())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("update BaseModel {} name \"test\"".format(obj_id))
            self.assertIn("test", f.getvalue())

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            self.assertIn("Invalid command", f.getvalue())

if __name__ == "__main__":
    unittest.main()
