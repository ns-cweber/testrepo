import unittest
from greet import greet

class GreetTests(unittest.TestCase):
    def test_greet(self):
        self.assertEqual("hello!", greet())
