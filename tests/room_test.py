import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("party room", 20, 1000)
        self.guest = Guest("Paul", 20, 100)
        self.guest_2 = Guest("James", 25, 120)
        self.guest_3 = Guest("Chris", 25, 200)
        self.song = Song("Live it up", "Mental as anything")
        self.song_2 = Song("Dignity", "Deacon Blue")

    def test_can_get_room_name(self):
        self.assertEqual("party room", self.room.name)


    def test_can_add_guest_to_room(self):
        self.room.new_guest(self.guest)
        self.assertEqual(1, self.room.has_guest())

    def test_can_remove_guest_from_room(self):
        self.room.new_guest(self.guest)
        self.room.new_guest(self.guest_2)
        self.room.remove_guest(self.guest)
        self.assertEqual(1, self.room.has_guest())
    
    def test_can_add_song_to_room(self):
        self.room.add_song(self.song)
        self.room.add_song(self.song_2)
        self.assertEqual(2, self.room.has_song())



    def test_can_take_money(self):
        self.room.customer_fee(20)
        self.assertEqual(1020, self.room.till)

    def test_room_capacity_false(self):
        self.room.new_guest(self.guest)
        self.room.new_guest(self.guest_2)
        self.room.new_guest(self.guest_3)
        self.assertEqual(False, self.room.check_capacity())

    def test_room_capacity_true(self):
        self.room.new_guest(self.guest)
        self.assertEqual(True, self.room.check_capacity())

    # def test_can_stop_entrance_when_full(self):
    #     self.room.new_guest(self.guest)
    #     self.room.new_guest(self.guest_2)
    #     self.room.check_capacity()
    #     self.room.new_guest(self.guest_3)
    #     self.room.check_capacity()
    #     self.room.new_guest(self.guest)
    #     self.room.check_capacity()
    #     self.room.new_guest(self.guest_2)
    #     self.room.check_capacity()
    #     self.assertEqual(2, self.room.has_guest())