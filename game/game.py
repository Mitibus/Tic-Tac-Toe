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
            if self.is_winner(row, col):
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

    def is_winner(self, row, col):
        # Check row only if the last move was in that row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
            self.win_position = f"r:{row}"
            return True

        # Check column only if the last move was in that column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
            self.win_position = f"c:{col}"
            return True

        # Check diagonals only if the last move was in that diagonal
        if row == col:  # Left diagonal
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
                self.win_position = "d:0"
                return True

        if row + col == 2:  # Right diagonal
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
                self.win_position = "d:1"
                return True

        return False

    def is_tie(self):
        return np.all(self.board != '')

    def play(self):
        if self.current_player.is_ai:
            self.current_player.make_move(self)
