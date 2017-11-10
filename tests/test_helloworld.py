import unittest
FAILURE = 'incorrect value'

class HelloTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_hello(self):
        self.assertEqual("hello", "hellos", FAILURE)
