#!/usr/bin/python3
"""
Defines unittests for models/engine/file_storage.py.
"""

import unittest
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Unittest to set up necessary objects or configurations"""
        self.file_storage = FileStorage()

    def tearDown(self):
        """Unittest to Clean up after each test"""
        pass

    def test_all_method(self):
        """Unittest to test the 'all' method of FileStorage"""
        all_objects = self.file_storage.all()
        
    def test_new_method(self):
        """Unittest to test the 'new' method of FileStorage"""
        mock_obj = MagicMock(spec=BaseModel)
        mock_obj.id = 'mock_id' 
        self.file_storage.new(mock_obj)
        
    def test_save_method(self):
        """Unittest to test the 'save' method of FileStorage"""
        self.file_storage.save()
        
    def test_reload_method(self):
        """Unittest to test the 'reload' method of FileStorage"""
        self.file_storage.reload()
        
if __name__ == '__main__':
    unittest.main()

