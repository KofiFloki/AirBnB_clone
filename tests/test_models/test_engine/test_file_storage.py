#!/usr/bin/python3
"""
Unittest to test the FileStorage class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from uuid import uuid4


class TestFileStorage(unittest.TestCase):
    """Testing file storage"""

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """test the instance"""
        store = FileStorage()
        self.assertIsInstance(store, FileStorage)

    def test_all(self):
        """tests the all function in Filestorage"""
        store = FileStorage()
        store_dict = store.all()
        self.assertIsNotNone(store_dict)
        self.assertIs(store_dict, store._FileStorage__objects)
        self.assertEqual(type(store_dict), dict)

    def test_new(self):
        """tests the new function in FileStorage"""
        store = FileStorage()
        store_dict = store.all()
        state = State()
        state.id = uuid4()
        state.name = "Edo"
        store.new(state)
        key = "State." + str(state.id)
        self.assertIsNotNone(store_dict[key])

    def test_doc(self):
        """tests if all function are documented"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.reload)
        self.assertIsNotNone(FileStorage)

    def test_reload(self):
        """tests the reload function in FileStorage"""
        store = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as myFile:
            myFile.write("{}")
        with open("file.json", "r") as readFile:
            for string in readFile:
                self.assertEqual(string, "{}")
        self.assertIs(store.reload(), None)


if __name__ == "__main__":
    unittest.main()
