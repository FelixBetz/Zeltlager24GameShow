"""list game"""

from flask import Blueprint, jsonify, request
from src.games.list_game.list_game_model import ListGameState
from src.data import list_game_data, dummy_data, current_game

list_game = Blueprint(
    "list_Game",
    __name__,
)


@list_game.route("/api/list_game/data")
def get_list_game_data():
    """get list game data"""
    return jsonify(list_game_data.get_json())


@list_game.route("/api/list_game/place", methods=["POST"])
def place_item():
    """place item into list"""

    place_index = int(request.form.get("index"))
    place_position = int(request.form.get("position"))

    ret = list_game_data.place_by_index(place_index, place_position)

    return jsonify(ret)


@list_game.route("/api/list_game/switchState")
def switch_state():
    """get list game data"""
    new_state_str = request.args.get("state", None)
    if new_state_str:
        new_state = ListGameState(new_state_str)

        # entry state actions
        if new_state == ListGameState.PLAY:
            if 0 <= current_game.current_turn_team < len(current_game.teams):
                list_game_data.start_game(dummy_data)

        list_game_data.switch_state(new_state)

    return jsonify(list_game_data.state.name)
