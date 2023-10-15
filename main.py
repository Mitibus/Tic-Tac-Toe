import pygame
from screen import Screen
from game.constants import WINNER_EVENT, TIE_EVENT

pygame.init()
screen = Screen()

running = True
while running:
    screen.state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                screen.click_on_screen()

        if event.type == WINNER_EVENT:
            screen.game.is_winner = True
            screen.state = screen.end_game_screen

        if event.type == TIE_EVENT:
            screen.game.is_winner = False
            screen.state = screen.end_game_screen

    for button in screen.buttons:
        button.process()

    pygame.display.update()

pygame.quit()
