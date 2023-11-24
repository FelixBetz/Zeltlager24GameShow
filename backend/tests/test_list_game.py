"""unit test models schema"""
import unittest

from src.games.list_game.list_game_model import (
    ListGameItem,
    ListGameData,
    ListGameState,
)

TEST_GAME_DATA = [
    {"label": "test1", "value": -1},
    {"label": "test2", "value": 0},
    {"label": "test3", "value": 1},
    {"label": "test4", "value": 2},
]


class TestListGame(unittest.TestCase):
    """test dummy"""

    def test_list_game_item(self):
        """test list game item"""
        my_list_game = ListGameItem("Test", 1234)
        self.assertEqual(my_list_game.label, "Test")
        self.assertEqual(my_list_game.value, 1234)
        self.assertEqual(my_list_game.index, -1)
        self.assertEqual(my_list_game.random_index, -1)
        self.assertFalse(my_list_game.is_placed)
        self.assertFalse(my_list_game.is_start_item)

        self.assertEqual(
            my_list_game.to_json(),
            {
                "label": "Test",
                "value": 1234,
                "index": -1,
                "isPlaced": False,
                "isStartItem": False,
                "isShowValue": False,
            },
        )

        self.assertEqual(repr(my_list_game), "Test:False")

    def test_list_game_start(self):
        """test list game start"""
        my_game_data = ListGameData()

        self.assertEqual(my_game_data.data, [])

        my_game_data.start_game(TEST_GAME_DATA)

        # check indices
        indices = [item.index for item in my_game_data.data]
        self.assertEqual(indices, [0, 1, 2, 3])

        # check random indices
        random_indices = [item.random_index for item in my_game_data.data]
        random_indices.sort()
        self.assertEqual(random_indices, [0, 1, 2, 3])

        # only one item should be marked as start item and placed
        placed_objects = [item for item in my_game_data.data if item.is_placed]
        self.assertEqual(len(placed_objects), 1)
        start_items = [item for item in my_game_data.data if item.is_start_item]
        self.assertEqual(len(start_items), 1)

    def test_list_game_get_json(self):
        """test list game get json"""
        my_game_data = ListGameData()
        my_game_data.start_game(TEST_GAME_DATA)

        json_dict = my_game_data.get_json()

        self.assertEqual(len(json_dict["itemsSorted"]), 4)
        self.assertEqual(len(json_dict["placedItems"]), 1)
        self.assertEqual(len(json_dict["itemsRandom"]), 3)
        self.assertEqual(json_dict["minValue"], 1970)
        self.assertEqual(json_dict["maxValue"], 2023)
        self.assertEqual(
            json_dict["question"], "Ordne die Zeltlager nach der Jahreszahl"
        )

    def test_list_place_data(self):
        """test list place data"""
        my_game_data = ListGameData()

        # get GameData where Start Index is 2
        while True:
            my_game_data.start_game(TEST_GAME_DATA)
            for item in my_game_data.data:
                if item.is_start_item:
                    start_index = item.index
                    break
            if start_index == 2:
                break

        # try to already placed item
        my_game_data.place_by_index(2, 1)
        idx_placed = [item.index for item in my_game_data.data if item.is_placed]
        self.assertEqual(idx_placed, [2])

        # flase place
        my_game_data.place_by_index(3, 1)
        idx_placed = [item.index for item in my_game_data.data if item.is_placed]
        self.assertEqual(idx_placed, [2])

        # place before
        my_game_data.place_by_index(0, 1)
        idx_placed = [item.index for item in my_game_data.data if item.is_placed]
        self.assertEqual(idx_placed, [0, 2])

        # place after
        my_game_data.place_by_index(3, 3)
        idx_placed = [item.index for item in my_game_data.data if item.is_placed]
        self.assertEqual(idx_placed, [0, 2, 3])

        # place after
        my_game_data.place_by_index(1, 2)
        idx_placed = [item.index for item in my_game_data.data if item.is_placed]
        self.assertEqual(idx_placed, [0, 1, 2, 3])
        idx_unplaced = [item.index for item in my_game_data.data if not item.is_placed]
        self.assertEqual(idx_unplaced, [])

    def test_switch_state(self):
        """test switcht state"""

        my_game_data = ListGameData()
        self.assertEqual(my_game_data.state, ListGameState.IDLE)
        my_game_data.switch_state(ListGameState.WAIT_DRAW)
        self.assertEqual(my_game_data.state, ListGameState.WAIT_DRAW)
