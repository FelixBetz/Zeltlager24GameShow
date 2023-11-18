"""list game"""

from flask import Blueprint, jsonify, request
from src.data import list_game_data

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
