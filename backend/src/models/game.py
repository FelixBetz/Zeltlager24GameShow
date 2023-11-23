"""handles all game informations"""

from enum import Enum


class GameState(Enum):
    """all game states"""

    IDLE = "IDLE"
    CREATING_TEAMS = "CREATING_TEAMS"
    GAME_1 = "GAME_1"
    GAME_2 = "GAME_2"
    GAME_3 = "GAME_3"
    GAME_4 = "GAME_4"
    GAME_5 = "GAME_5"
    SCORE = "SCORE"


class Team:
    """represents a team"""

    def __init__(self, arg_name="", arg_shortcut="", arg_avatar_url=""):
        self.name = arg_name
        self.name_shortcut = arg_shortcut
        self.avatar_url = arg_avatar_url
        self.scores = []  # Array of scores
        self.game_life = 3

    def get_score(self):
        """returns total team score"""
        return sum(self.scores)

    def to_json(self):
        """returns object as json"""
        return {
            "name": self.name,
            "shortcut": self.name_shortcut,
            "avatar_url": self.avatar_url,
            "scores": self.scores,
            "total_score": self.get_score(),
            "game_life": self.game_life,
        }

    def reset(self):
        """reset data"""
        self.name = ""
        self.name_shortcut = ""
        self.avatar_url = ""
        self.scores = []

    def add_score(self, arg_score):
        """add score"""
        self.scores.append(arg_score)


class Game:
    """represents a game"""

    def __init__(self):
        self.teams = []
        self.game_state = GameState.IDLE
        self.current_turn_team = -1

    def change_game_state(self, new_state):
        """change game state"""
        self.game_state = new_state

    def add_team(self, arg_team):
        """adds a team"""
        self.teams.append(arg_team)

    def to_json(self):
        """game to json"""
        return {
            "state": self.game_state.name,
            "teams": [team.to_json() for team in self.teams],
            "currentTurnTeam": self.current_turn_team,
        }
