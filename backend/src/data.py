"""handles the global data objects"""

from src.games.list_game.list_game_model import ListGameData
from src.models.game import Game, Team


GAMES_TO_PLAY = 5

current_game = Game(GAMES_TO_PLAY)
current_team = Team()

list_game_data = ListGameData()


dummy_data = [
    {"label": "Zeltlager 2011", "value": 2011},
    {"label": "Zeltlager 2012", "value": 2012},
    {"label": "Zeltlager 2013", "value": 2013},
    {"label": "Zeltlager 2014", "value": 2014},
    {"label": "Zeltlager 2015", "value": 2015},
    {"label": "Zeltlager 2016", "value": 2016},
    {"label": "Zeltlager 2018", "value": 2018},
    {"label": "Zeltlager 2017", "value": 2017},
    {"label": "Zeltlager 2019", "value": 2019},
    {"label": "Zeltlager 2020", "value": 2020},
]
