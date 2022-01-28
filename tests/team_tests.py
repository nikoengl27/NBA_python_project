import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Toronto Raptors", "Scotiabank Arena", 23, 23)
    
    def team_has_name(self):
        self.assertEqual("Toronto Raptors", self.team.name)
    
    def team_has_stadium(self):
        self.assertEqual("Scotiabank Arena", self.team.stadium)
    
    def team_has_wins(self):
        self.assertEqual(23, self.team.wins)
    
    def team_has_losses(self):
        self.assertEqual(23, self.team.losses)
