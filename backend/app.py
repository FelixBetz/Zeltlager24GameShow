"""
filename: app.py
contains all flask routes
"""
import logging
import random
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


@app.route("/api/admin/decrementLife")
def increase_team_life():
    """switch current team turn"""
    team_idx = int(request.args.get("team", -1))
    if 0 <= team_idx < len(current_game.teams):
        return jsonify(current_game.teams[team_idx].decrement_life())
    return jsonify(False)


@app.route("/api/admin/incrementLife")
def decrease_team_life():
    """switch current team turn"""
    team_idx = int(request.args.get("team", -1))
    if 0 <= team_idx < len(current_game.teams):
        return jsonify(current_game.teams[team_idx].increment_life())
    return jsonify(False)


def test_setup():
    """setup test enviorement"""

    team1 = Team("Gewinner", "T1", "avatars/owl.png")
    team2 = Team("Trinity", "T2", "avatars/bird.png")
    team3 = Team("Test", "T3", "avatars/lion.png")

    my_array = [1, 2, 3]
    for _ in range(5):
        # Shuffle the array randomly
        random.shuffle(my_array)
        team1.add_score(my_array[0])
        team2.add_score(my_array[1])
        team3.add_score(my_array[2])

    current_game.add_team(team1)
    current_game.add_team(team2)
    current_game.add_team(team3)

    current_game.change_game_state(GameState.IDLE)
    current_game.games_played = 3


if __name__ == "__main__":
    test_setup()
    app.run(
        debug=True,
        port=8080,
        host="0.0.0.0",
    )
