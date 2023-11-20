"""handles all list game models"""

from enum import Enum
import random


class ListGameState(Enum):
    """all game states"""

    IDLE = "IDLE"
    WAIT_DRAW = "WAIT_DRAW"
    PLAY = "PLAY"
    SHOW_POINTS = "SHOW_POINTS"


class ListGameData:
    """list game data game"""

    def __init__(self):
        self.data = []
        self.state = ListGameState.IDLE

    def switch_state(self, arg_state):
        """change state"""
        self.state = arg_state

    def start_game(self, arg_data):
        """start game"""
        self.data = []
        for item in arg_data:
            self.data.append(ListGameItem(item["label"], item["value"]))

        # sort by value and save indices
        self.data = sorted(self.data, key=lambda x: x.value)
        for idx, item in enumerate(self.data):
            item.index = idx

        # randomly choose start item
        start_index = random.randint(0, len(self.data) - 1)
        self.data[start_index].is_placed = True
        self.data[start_index].is_start_item = True

        # create random indices
        indices = list(range(0, len(self.data)))

        random.shuffle(indices)

        for idx, item in enumerate(self.data):
            item.random_index = indices[idx]

    def place_by_index(self, arg_index, arg_pos):
        """place item by index"""

        sorted_placed_data = [item for item in self.data if item.is_placed]

        # calculate previous/next placed_data index
        # frontend starts counting from 1
        arg_pos -= 1
        idx_prev = arg_pos - 1
        idx_next = arg_pos

        if self.data[arg_index].is_placed:
            return False

        place_val = self.data[arg_index].value

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
            self.data[arg_index].is_placed = True

        return is_ok

    def get_json(self):
        """get game data as json"""
        # sort by value
        game_data_json = [item.to_json() for item in self.data]
        placed_item_json = [item.to_json() for item in self.data if item.is_placed]

        # sort by value

        random_sorted_json = [
            item.to_json()
            for item in sorted(self.data, key=lambda x: x.random_index)
            if not item.is_start_item
        ]

        return {
            "state": self.state.name,
            "itemsSorted": game_data_json,
            "placedItems": placed_item_json,
            "itemsRandom": random_sorted_json,
            "minValue": 1970,  # todo
            "maxValue": 2023,  # todo
            "question": "Ordne die Zeltlager nach der Jahreszahl",  # todo
        }


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
