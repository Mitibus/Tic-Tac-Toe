import numpy as np
import random


class Player:
    def __init__(self, name, symbol, is_ai=False):
        self.name = name
        self.symbol = symbol
        self.is_ai = is_ai

    def make_move(self, game, row=None, col=None):
        if self.is_ai:
            empty_positions = np.argwhere(game.board == '')
            row, col = random.choice(empty_positions)

        game.make_move(row, col, self)
