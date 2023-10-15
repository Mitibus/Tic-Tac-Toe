import numpy as np
import random


class Player:
    def __init__(self, name, symbol, is_ai=False):
        self.name = name
        self.symbol = symbol
        self.is_ai = is_ai

    def make_move(self, game, row=None, col=None):
        if self.is_ai:
            row, col = self.bestMove(game.board)

        game.make_move(row, col, self)

    def bestMove(self, board):
        bestMove = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = self.symbol
                    score = self.minimax(board, 0, False)
                    board[i][j] = ''
                    if bestMove is None or score > bestMove[0]:
                        bestMove = (score, i, j)
        return (bestMove[1], bestMove[2])

    def minimax(self, board, depth, isMaximizing):
        result = self.check_winner(board)
        if result is not None:
            if result == self.symbol:
                return 1
            elif result == 'tie':
                return 0
            else:
                return -1

        if isMaximizing:
            bestScore = -np.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = self.symbol
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ''
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = np.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'O' if self.symbol == 'X' else 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ''
                        bestScore = min(score, bestScore)
            return bestScore

    def check_winner(self, board):
        # Check rows
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '':
                return board[i][0]

        # Check columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != '':
                return board[0][i]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != '':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '':
            return board[0][2]

        # Check tie
        if np.all(board != ''):
            return 'tie'

        return None
