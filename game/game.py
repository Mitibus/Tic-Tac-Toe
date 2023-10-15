import random
import numpy as np
import pygame
from game.constants import WINNER_EVENT, TIE_EVENT


class TicTacToe:
    def __init__(self, players):
        self.board = np.empty((3, 3), dtype=str)
        self.players = players
        self.current_player = random.choice(self.players)

    def print_board(self):
        print(self.board)

    def make_move(self, row, col, player):
        if self.is_cell_available(row, col):
            self.board[row][col] = player.symbol

            # Check if there is a winner
            if self.is_winner():
                # Create a custom event
                event = pygame.event.Event(
                    WINNER_EVENT, message=f"{player.name} won!", win_positions=self.win_position)
                pygame.event.post(event)
            elif self.is_tie():
                event = pygame.event.Event(TIE_EVENT, message="Tie!")
                pygame.event.post(event)
            else:
                self.current_player = self.get_next_player()
                if self.current_player.is_ai:
                    self.current_player.make_move(self)

    def is_cell_available(self, row, col):
        print(type(self.board), type(row), type(col))
        print(self.board[row][col])
        return self.board[row][col] == ''

    def get_next_player(self):
        return self.players[0] if self.current_player == self.players[1] else self.players[1]

    def is_winner(self):
        # Check rows
        for i in range(3):
            row = self.board[i]
            if row[0] == row[1] == row[2] != '':
                self.win_position = f"r:{i}"
                return True

        # Check columns
        for i in range(3):
            col = self.board[:, i]
            if col[0] == col[1] == col[2] != '':
                self.win_position = f"c:{i}"
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.win_position = "d:0"
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.win_position = "d:1"
            return True

        return False

    def is_tie(self):
        return np.all(self.board != '')

    def play(self):
        if self.current_player.is_ai:
            self.current_player.make_move(self)
