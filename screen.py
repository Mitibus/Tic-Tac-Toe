import pygame
from components.button import Button
from game.player import Player
from game.game import TicTacToe

# BG_COLOR = "#16BDAC"
# MAIN_COLOR = "#0CA192"
# BUTTON_HOVERED_COLOR = "#00af9b"

BG_COLOR = "#015958"
MAIN_COLOR = "#008F8C"
BUTTON_HOVERED_COLOR = "#023535"
RED = "#FF0000"


class Screen:
    def __init__(self, size=(1280, 720)):
        self.screen = pygame.display.set_mode(size)
        # Add a title to the window
        pygame.display.set_caption("Tic Tac Toe")
        self.state = self.main_screen
        self.buttons = pygame.sprite.Group()

    def main_screen(self):
        self.buttons = pygame.sprite.Group()

        # Set background color
        self.screen.fill(BG_COLOR)

        # Draw title
        title = self.get_font(100).render("Tic Tac Toe", True, MAIN_COLOR)
        title_rect = title.get_rect(center=(640, 100))
        self.screen.blit(title, title_rect)

        # Draw buttons
        human_button = Button(
            self.screen,
            position=(640 - 150, 250),
            size=(300, 100),
            text="Human vs Human",
            background_color=BG_COLOR,
            text_color=MAIN_COLOR,
            hovered_color=BUTTON_HOVERED_COLOR,
            font_size=50,
            on_click_function=self.start_game_2_players
        )

        ai_button = Button(
            self.screen,
            position=(640 - 150, 400),
            size=(300, 100),
            text="Human vs AI",
            background_color=BG_COLOR,
            text_color=MAIN_COLOR,
            hovered_color=BUTTON_HOVERED_COLOR,
            font_size=50,
            on_click_function=self.start_game_against_ai
        )

        quit_button = Button(
            self.screen,
            position=(640 - 150, 550),
            size=(300, 100),
            text="Quit",
            background_color=BG_COLOR,
            text_color=MAIN_COLOR,
            hovered_color=BUTTON_HOVERED_COLOR,
            font_size=50,
            on_click_function=self.quit
        )

        self.buttons.add(human_button, ai_button, quit_button)

    def start_game_2_players(self):
        self.is_playing_against_ai = False
        self.start_game()

    def start_game_against_ai(self):
        self.is_playing_against_ai = True
        self.start_game()

    def play_screen(self):
        # Set background color
        self.screen.fill(BG_COLOR)

        # Draw title
        title = self.get_font(70).render("Tic Tac Toe", True, MAIN_COLOR)
        title_rect = title.get_rect(center=(300, 100))
        self.screen.blit(title, title_rect)

        # Draw the board
        self.draw_board()

    def draw_board(self):
        # Draw the game board
        self.game_board = pygame.Surface((600, 600))
        self.game_board.fill(BG_COLOR)

        # Draw the lines
        pygame.draw.line(self.game_board, MAIN_COLOR, (200, 0), (200, 600), 10)
        pygame.draw.line(self.game_board, MAIN_COLOR, (400, 0), (400, 600), 10)
        pygame.draw.line(self.game_board, MAIN_COLOR, (0, 200), (600, 200), 10)
        pygame.draw.line(self.game_board, MAIN_COLOR, (0, 400), (600, 400), 10)

        # Draw the board
        self.screen.blit(self.game_board, (0, 200))

        for row in range(3):
            for col in range(3):
                symbol = self.game.board[row][col]
                if symbol != "":
                    symbol_surface = self.get_font(
                        100).render(symbol, True, MAIN_COLOR)
                    symbol_rect = symbol_surface.get_rect(
                        center=(col * 200 + 100, row * 200 + 100 + 200))
                    self.screen.blit(symbol_surface, symbol_rect)

    def start_game(self):
        self.screen = pygame.display.set_mode((600, 800))
        self.buttons.empty()
        self.state = self.play_screen

        if self.is_playing_against_ai:
            player_1 = Player("Human", "X")
            player_2 = Player("AI", "O", is_ai=True)
        else:
            player_1 = Player("Player 1", "X")
            player_2 = Player("Player 2", "O")

        self.game = TicTacToe([player_1, player_2])
        self.game.play()

    def click_on_screen(self):
        print("Clicked on screen")
        if self.state == self.play_screen:
            # Get the position of the mouse
            mouse_position = pygame.mouse.get_pos()

            # Check if the mouse is on the board
            if mouse_position[1] > 200:
                # Get the row and column of the cell
                row = (mouse_position[1] // 200) - 1
                col = mouse_position[0] // 200

                # Check if the game mode is against AI
                if self.is_playing_against_ai and not self.game.current_player.is_ai:
                    # Make the move
                    self.game.current_player.make_move(
                        self.game, row=row, col=col)
                elif not self.is_playing_against_ai:
                    self.game.current_player.make_move(
                        self.game, row=row, col=col)

        elif self.state == self.end_game_screen:
            self.screen = pygame.display.set_mode((1280, 720))
            self.state = self.main_screen

    def end_game_screen(self):
        # Set background color
        self.screen.fill(BG_COLOR)

        # Draw the board
        self.draw_board()

        message = None
        if self.game.is_winner:
            message = f"{self.game.current_player.name} won!"
            win_positions = self.game.win_position
        else:
            message = "Tie!"
            win_positions = None

        # Draw the message
        message_surface = self.get_font(70).render(message, True, MAIN_COLOR)
        message_rect = message_surface.get_rect(center=(300, 100))
        self.screen.blit(message_surface, message_rect)

        if win_positions:
            # Draw the win positions
            switcher = {
                "r:0": [(100, 300), (500, 300)],
                "r:1": [(100, 500), (500, 500)],
                "r:2": [(100, 700), (500, 700)],
                "c:0": [(100, 300), (100, 700)],
                "c:1": [(300, 300), (300, 700)],
                "c:2": [(500, 300), (500, 700)],
                "d:0": [(100, 300), (500, 700)],
                "d:1": [(500, 300), (100, 700)],
            }

            # Draw the line
            pygame.draw.line(self.screen, RED,
                             switcher[win_positions][0], switcher[win_positions][1], 10)

    def quit(self):
        # Quit the game by generating a QUIT event
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def get_font(self, size):
        return pygame.font.SysFont("assets/TechnoRaceItalic.otf", size)
