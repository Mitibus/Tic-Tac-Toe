from player import Player
from game import Game

print("Welcome to Tic Tac Toe!\n In which mode do you want to play?\n 1. Player vs Player\n 2. Player vs AI")
mode = input("Enter 1 or 2: ")

if mode == "1":
    player1 = Player(input("Enter player 1 name: "), "X")
    player2 = Player(input("Enter player 2 name: "), "O")
elif mode == "2":
    player1 = Player(input("Enter player name: "), "X")
    player2 = Player("AI", "O", True)
else:
    print("Invalid mode")
    exit()

print("Let's start the game!")
game = Game([player1, player2])
game.play()
