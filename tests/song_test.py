import unittest
from src.song import   Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Last Nite", "The Strokes")

    def test_get_song_name(self):
        self.assertEqual("Last Nite", self.song.name)

    def test_get_song_title(self):
        self.assertEqual("The Strokes", self.song.artist)