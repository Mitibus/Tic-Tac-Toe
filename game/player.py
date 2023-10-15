import numpy as np
import random


class Player:
    def __init__(self, name, symbol, is_ai=False):
        self.name = name
        self.symbol = symbol
        self.is_ai = is_ai
        self.memorisation = {}

    def make_move(self, game, row=None, col=None):
        if self.is_ai:
            row, col = self.bestMove(game.board)

        game.make_move(row, col, self)

    def bestMove(self, board):
        bestMove = None
        alpha = -np.inf
        beta = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = self.symbol
                    score = self.minimax(
                        board, 0, False, alpha, beta, row=i, col=j)
                    board[i][j] = ''
                    if bestMove is None or score > bestMove[0]:
                        bestMove = (score, i, j)
        return (bestMove[1], bestMove[2])

    def minimax(self, board, depth, isMaximizing, alpha, beta, row=None, col=None):
        boad_str = np.array2string(board)
        if boad_str in self.memorisation:
            return self.memorisation[boad_str]

        result = self.check_winner(board, row, col)
        if result is not None:
            if result == self.symbol:
                self.memorisation[boad_str] = 1
                return 1
            elif result == 'tie':
                self.memorisation[boad_str] = 0
                return 0
            else:
                self.memorisation[boad_str] = -1
                return -1

        preferred_moves = [(1, 1), (0, 0), (0, 2), (2, 0),
                           (2, 2), (0, 1), (1, 0), (1, 2), (2, 1)]

        if isMaximizing:
            bestScore = -np.inf
            for move in preferred_moves:
                i, j = move
                if board[i][j] == '':
                    board[i][j] = self.symbol
                    score = self.minimax(
                        board, depth + 1, False, alpha, beta, row=i, col=j)
                    board[i][j] = ''
                    bestScore = max(score, bestScore)
                    alplha = max(alpha, score)
                    if beta <= alpha:
                        return bestScore
            self.memorisation[boad_str] = bestScore
            return bestScore
        else:
            bestScore = np.inf
            for move in preferred_moves:
                i, j = move
                if board[i][j] == '':
                    board[i][j] = 'O' if self.symbol == 'X' else 'X'
                    score = self.minimax(
                        board, depth + 1, True, alpha, beta, row=i, col=j)
                    board[i][j] = ''
                    bestScore = min(score, bestScore)
                    beta = min(beta, score)
                    if beta <= alpha:
                        return bestScore
            self.memorisation[boad_str] = bestScore
            return bestScore

    def check_winner(self, board, row, col):
        # Check the row where the last move was made
        if board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]

        # Check the column where the last move was made
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

        # Check the diagonal where the last move was made
        if row == col:  # Move was made on the left diagonal
            if board[0][0] == board[1][1] == board[2][2]:
                return board[0][0]

        if row + col == 2:  # Move was made on the right diagonal
            if board[0][2] == board[1][1] == board[2][0]:
                return board[0][2]

        # Check if the board is full
        if np.all(board != ''):
            return 'tie'

        return None
