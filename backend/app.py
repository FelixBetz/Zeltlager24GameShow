"""
filename: app.py
contains all flask routes
"""
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from src.games.list_game.list_game_model import ListGameState
from src.models.game import GameState
from src.create_teams import create_teams
from src.frontend import frontend
from src.data import current_game, list_game_data
from src.models.game import Team
from src.games.list_game.list_game import list_game

app = Flask(__name__)
cors = CORS(app)


log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app.config["AVATAR_DIR"] = "static/assets/avatars"
app.register_blueprint(create_teams)
app.register_blueprint(frontend)
app.register_blueprint(list_game)


# game
@app.route("/api/game")
def api_get_game_state():
    """returns current game state"""
    return jsonify(current_game.to_json())


@app.route("/api/admin/switchState")
def api_admin_switch_state():
    """swtich state"""
    new_state_str = request.args.get("state", None)
    if new_state_str:
        new_state = GameState(new_state_str)

        # entry state actions
        if new_state == GameState.GAME_1:
            list_game_data.switch_state(ListGameState.IDLE)

        current_game.change_game_state(new_state)

    return jsonify(current_game.game_state.name)


@app.route("/api/admin/switchCurrentTurn")
def switch_current_team_turn():
    """switch current team turn"""
    team_idx = int(request.args.get("team", -1))
    if -1 <= team_idx < len(current_game.teams):
        current_game.current_turn_team = team_idx
        return jsonify(True)

    return jsonify(False)


def test_setup():
    """setup test enviorement"""

    team1 = Team("Team1", "T1", "avatars/owl.png")
    current_game.add_team(team1)

    team2 = Team("Team2", "T2", "avatars/bird.png")
    current_game.add_team(team2)

    team2 = Team("Team3", "T3", "avatars/lion.png")
    current_game.add_team(team2)

    current_game.change_game_state(GameState.CREATING_TEAMS)


if __name__ == "__main__":
    test_setup()
    app.run(
        debug=True,
        port=8080,
        host="0.0.0.0",
    )
