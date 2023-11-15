"""list game"""

import copy
import random
from enum import Enum
from flask import Blueprint, jsonify, request


class GameState(Enum):
    """all game states"""

    IDLE = "IDLE"
    WAIT_DRAW = "WAIT_DRAW"
    GAME_1 = "PLAY"
    GAME_2 = "SHOW_POINTS"


class ListGameItem:
    """ListGameItem"""

    def __init__(self, arg_label, arg_value):
        self.label = arg_label
        self.value = arg_value
        self.index = -1
        self.random_index = -1
        self.is_placed = False
        self.is_start_item = False

    def to_json(self):
        """convert to json"""
        return {
            "label": self.label,
            "value": self.value,
            "index": self.index,
            "isPlaced": self.is_placed,
            "isStartItem": self.is_start_item,
        }

    def __repr__(self):
        return self.label + ":" + str(self.is_placed)


list_game = Blueprint(
    "list_Game",
    __name__,
)

dummy_data = [
    ListGameItem("Zeltlager 2011", 2011),
    ListGameItem("Zeltlager 2012", 2012),
    ListGameItem("Zeltlager 2013", 2013),
    ListGameItem("Zeltlager 2014", 2014),
    ListGameItem("Zeltlager 2015", 2015),
    # ListGameItem("Zeltlager 2016", 2016),
    # ListGameItem("Zeltlager 2018", 2018),
    # ListGameItem("Zeltlager 2017", 2017),
    # ListGameItem("Zeltlager 2019", 2019),
    # ListGameItem("Zeltlager 2020", 2020),
]


game_data = []


def place_by_index(arg_index, arg_pos):
    """place item by index"""
    global game_data

    sorted_placed_data = [item for item in game_data if item.is_placed]

    # calculate previous/next placed_data index
    # frontend starts counting from 1
    arg_pos -= 1
    idx_prev = arg_pos - 1
    idx_next = arg_pos

    place_val = game_data[arg_index].value

    # get previous item value and next item value
    if idx_prev >= 0:
        prev_val = sorted_placed_data[idx_prev].value
    else:
        prev_val = float("-inf")

    if idx_next < len(sorted_placed_data):
        next_val = sorted_placed_data[idx_next].value
    else:
        next_val = float("+inf")

    # check if item is placed correctly
    is_ok = prev_val <= place_val <= next_val

    # mark as places if position is correct
    if is_ok:
        game_data[arg_index].is_placed = True

    return is_ok


def start_game_1():
    """start game"""

    global game_data
    game_data = []
    game_data = copy.deepcopy(dummy_data)

    # sort by value and save indices
    game_data = sorted(game_data, key=lambda x: x.value)
    for idx, item in enumerate(game_data):
        item.index = idx

    # randomly choose start item
    start_index = random.randint(0, len(game_data) - 1)
    game_data[start_index].is_placed = True
    game_data[start_index].is_start_item = True

    # create random indices
    indices = list(range(0, len(game_data)))

    random.shuffle(indices)

    for idx, item in enumerate(game_data):
        item.random_index = indices[idx]

    return jsonify("ok")


@list_game.route("/api/list_game/data")
def get_list_game_data():
    """get list game data"""
    global game_data

    # sort by value
    game_data_json = [item.to_json() for item in game_data]
    placed_item_json = [item.to_json() for item in game_data if item.is_placed]

    # sort by value

    random_sorted_json = [
        item.to_json()
        for item in sorted(game_data, key=lambda x: x.random_index)
        if not item.is_start_item
    ]

    return jsonify(
        {
            "itemsSorted": game_data_json,
            "placedItems": placed_item_json,
            "itemsRandom": random_sorted_json,
            "minValue": 1970,  # todo
            "maxValue": 2023,  # todo
            "question": "Ordne die Zeltlager nach der Jahreszahl",  # todo
        }
    )


@list_game.route("/api/list_game/place", methods=["POST"])
def place_item():
    """place item into list"""
    place_index = request.args.get("index", None)

    place_index = int(request.form.get("index"))
    place_position = int(request.form.get("position"))

    ret = place_by_index(place_index, place_position)

    return jsonify(ret)
