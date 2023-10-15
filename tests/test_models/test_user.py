#!/usr/bin/python3
"""
Unittest for user.py
"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up any necessary objects or configurations"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test"""
        pass

    def testHasAttributes(self):
        """Test if attributes exist"""
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))

    def test_attributes(self):
        """Test the attributes of the User class"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attributes_update(self):
        """Test updating the attributes of the User class"""

        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
