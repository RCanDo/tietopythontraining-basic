import unittest

from valid_email import *

class TestValidEmail(unittest.TestCase):

    def test_00_too_short(self):
        with self.assertRaises(ValueError):
            valid_email('a@b')

    def test_01_the_shortest(self):
        self.assertTrue(valid_email('a@b.c'))

    def test_02_little_longer_1(self):
        self.assertTrue(valid_email('a.b@c.d'))

    def test_03_using_dash(self):
        self.assertTrue(valid_email('a-b@c.d'))

    def test_04_dot_domain(self):
        with self.assertRaises(ValueError):
            valid_email('ab@.d')

    def test_03(self):
        self.assertTrue(valid_email('a-b@c-d.e'))

    def test_03(self):
        with self.assertRaises(ValueError):
            valid_email('a.@c')

if __name__ == "__main__":
    unittest.main()
