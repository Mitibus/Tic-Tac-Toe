import numpy as np
import random


class Player:
    def __init__(self, name, symbol, is_ai=False):
        self.name = name
        self.symbol = symbol
        self.is_ai = is_ai

    def make_move(self, game):
        move_made = False
        row, col = None, None
        while not move_made:
            if self.is_ai:
                empty_positions = np.argwhere(game.board == '')
                row, col = random.choice(empty_positions)
            else:
                print(
                    "Choose a position to place your symbol\n In which row do you want to place your symbol?")
                row = int(input("Enter row: "))
                print("In which column do you want to place your symbol?")
                col = int(input("Enter column: "))

            move_made = game.make_move(row, col, self)
