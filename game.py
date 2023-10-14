import random
import numpy as np


class Game:
    def __init__(self, players):
        self.board = np.empty((3, 3), dtype=str)
        self.players = players
        self.current_player = random.choice(self.players)

    def print_board(self):
        print(self.board)

    def make_move(self, row, col, player):
        if self.is_cell_available(row, col):
            self.board[row][col] = player.symbol
            return True
        else:
            print("Cell is not available")
            return False

    def is_cell_available(self, row, col):
        return self.board[row][col] == ''

    def get_next_player(self):
        return self.players[0] if self.current_player == self.players[1] else self.players[1]

    def is_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True

        # Check columns
        for col in self.board.T:
            if col[0] == col[1] == col[2] != '':
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def is_tie(self):
        return np.all(self.board != '')

    def play(self):
        while True:
            self.print_board()
            self.current_player.make_move(self)

            # Check if there is a winner
            if self.is_winner():
                print(f"{self.current_player.name} won!")
                break
            # Check if there is a tie
            elif self.is_tie():
                print("It's a tie!")
                break
            else:
                self.current_player = self.get_next_player()
