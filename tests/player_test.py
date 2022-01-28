import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("LA Clippers", "Kawhi Leonard", "SF")
    
    def test_player_has_team(self):
        self.assertEqual("LA Clippers", self.player.team)

    def test_player_has_name(self):
        self.assertEqual("Kawhi Leonard", self.player.name)

    def test_player_has_position(self):
        self.assertEqual("SF", self.player.position)
    
