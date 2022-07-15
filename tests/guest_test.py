import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John", 30)

    def test_get_guest_name(self):
        self.assertEqual("John", self.guest.name)

    def test_can_get_guest_age(self):
        self.assertEqual(30, self.guest.age)