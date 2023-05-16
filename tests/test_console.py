#!/usr/bin/python3
"""
Unittest for console interpreter
"""
import unittest
from io import StringIO
import os
import tests
import json
import console
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.engine.file_storage import FileStorage
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Unittest for console"""

    def setUp(self):
        """used to setup the test"""
        pass

    def tearDown(self):
        """used to tear down the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_doc(self):
        """tests the documentation in console"""
        self.assertIsNotNone(console.__doc__)

    def test_emptyline(self):
        """tests when there is no input"""
        inputs = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("\n")
            self.assertIs(output.getvalue(), "")

    def test_create(self):
    """Test the output for create"""
    self.console.onecmd("create BaseModel")
    expected_output = "[[BaseModel]"
    self.assertEqual(self.output.getvalue().strip(), expected_output)
    
    def test_console(self):
    """Test the output for console"""
    expected_output = "hbnb"
    with patch("sys.stdout", new=StringIO()) as output:
        self.console.onecmd("help")
        self.assertEqual(output.getvalue().strip(), expected_output)

    def test_show(self):
        """test the output for show"""
        inputs = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("show")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("show MyModel")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("show BaseModel")
            self.assertEqual(output.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("show BaseModel 121212")
            self.assertEqual(output.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("BaseModel.show('Bar')")
            self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_destroy(self):
        """test the output for destroy"""
        inputs = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("destroy")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("destroy MyModel")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("destroy BaseModel")
            self.assertEqual(output.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("destroy BaseModel 4030222910")
            self.assertEqual(output.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("BaseModel.destroy('4030222910')")
            self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_all(self):
        """test the output for all"""
        self.console.onecmd("all")
        expected_output = "[[City], [User], [State], [Place], [Amenity], [Review]]"
         self.assertEqual(self.output.getvalue().strip(), expected_output)

    def test_update(self):
        """test the output for update"""
        inputs = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("update")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("update Mymodel")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("update Place")
            self.assertEqual(output.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("update Place 121212")
            self.assertEqual(output.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("update")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def test_count(self):
        """test the output for count"""
        inputs = console.HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("create User")
            inputs.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("count User")
            self.assertEqual(output.getvalue(), "2\n")
        with patch('sys.stdout', new=StringIO()) as output:
            inputs.onecmd("User.count()")
            self.assertEqual(output.getvalue(), "2\n")


if __name__ == "__main__":
    unittest.main()
