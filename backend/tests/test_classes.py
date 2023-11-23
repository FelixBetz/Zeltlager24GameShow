"""unit test models schema"""
import unittest

from src.models.game import Team, Game, GameState


class TestClasses(unittest.TestCase):
    """test dummy"""

    def setUp(self):
        """set_up classes"""
        self.team1 = Team()
        self.team1.name = "Team A"
        self.team1.name_shortcut = "TA"
        self.team1.avatar_url = "https://example.com/teamA_avatar"
        self.team1.scores = [10, 15, 20]

        self.team2 = Team()
        self.team2.name = "Team B"
        self.team2.name_shortcut = "TB"
        self.team2.avatar_url = "https://example.com/teamB_avatar"
        self.team2.scores = [5, 25, 30]

        self.game = Game()

    def test_team__score(self):
        """test team score"""
        self.assertEqual(self.team1.get_score(), 45)
        self.assertEqual(self.team2.get_score(), 60)

        # add score
        self.team1.add_score(5)
        self.assertEqual(self.team1.scores, [10, 15, 20, 5])
        self.assertEqual(self.team1.get_score(), 50)

    def test_team_to_json(self):
        """test json conversion"""
        team_json = self.team1.to_json()
        self.assertEqual(team_json["name"], "Team A")
        self.assertEqual(team_json["shortcut"], "TA")
        self.assertEqual(team_json["avatar_url"], "https://example.com/teamA_avatar")
        self.assertEqual(team_json["scores"], [10, 15, 20])
        self.assertEqual(team_json["total_score"], 45)

    def test_change_game_state(self):
        """test change_game_state()"""
        self.game.change_game_state(GameState.CREATING_TEAMS)
        self.assertEqual(self.game.game_state, GameState.CREATING_TEAMS)

    def test_add_team(self):
        """test add_team()"""
        self.assertEqual(len(self.game.teams), 0)

        self.game.add_team(self.team1)
        self.assertEqual(len(self.game.teams), 1)

        self.game.add_team(self.team2)
        self.assertEqual(len(self.game.teams), 2)

    def test_game_to_json(self):
        """test convert game to json conversion"""
        self.game.change_game_state(GameState.GAME_1)
        self.game.add_team(self.team1)
        self.game.add_team(self.team2)

        game_json = self.game.to_json()
        self.assertEqual(game_json["state"], "GAME_1")
        self.assertEqual(len(game_json["teams"]), 2)

    def test_reset(self):
        """reset team data"""
        self.team1.reset()
        self.assertEqual(self.team1.name, "")
        self.assertEqual(self.team1.name_shortcut, "")
        self.assertEqual(self.team1.avatar_url, "")
        self.assertEqual(self.team1.get_score(), 0)
