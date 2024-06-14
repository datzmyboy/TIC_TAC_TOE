import pygame
from pygame.font import SysFont

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (600, 600)
screen = pygame.display.set_mode(window_size)


class Game:
    def __init__(self):
        self.window_size = (600, 700)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("2 Players")
        self.font = pygame.font.SysFont(None, 150)
        self.color_to_use = None
        self.hud_font = pygame.font.SysFont(None,100)
        self.game_state_font = pygame.font.SysFont(None,40)
        self.winner_font = pygame.font.SysFont(None,30)
        self.running,self.playing = True, False
        self.box1 = (0, 0, 200, 200)
        self.box2 = (200, 0, 200, 200)
        self.box3 = (400, 0, 200, 200)
        self.box4 = (0, 200, 200, 200)
        self.box5 = (200, 200, 200, 200)
        self.box6 = (400, 200, 200, 200)
        self.box7 = (0, 400, 200, 200)
        self.box8 = (200, 400, 200, 200)
        self.box9 = (400, 400, 200, 200)
        self.hud = (0, 600, 600, 100)
        self.box_states = [None] * 9  # Use None for empty, 'X' for X, 'O' for O
        self.x_turn = True  # X starts first
        self.row_1 = [" ", " ", " "]
        self.row_2 = [" ", " ", " "]
        self.row_3 = [" ", " ", " "]
        self.list_of_rows = [self.row_1, self.row_2, self.row_3]

        self.x_score = 0
        self.o_score = 0

        # self.is_pause = False
        self.game_over_bool = False
        self.draw =  False

        self.current_symbol = "X"
        self.win_text = self.game_state_font.render(f"Player {self.current_symbol} wins", True, (0, 0, 0))
        # self.score_updated = False

    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.is_pressed_function(event)
            self.screen.fill((0, 0, 0))
            self.draw_boxes()
            self.activate_box()
            self.draw_on_the_boxes()
            self.blit_hud()

            pygame.display.update()

    def blit_hud(self):
        hud_rect = pygame.Rect(self.hud)
        pygame.draw.rect(self.screen, (255, 255, 0), self.hud)

        x_score_text = self.hud_font.render(f"X: {self.x_score}", True, (0, 0, 0))
        o_score_text = self.hud_font.render(f"O: {self.o_score}", True, (0, 0, 0))

        screen_width, screen_height = self.window_size
        self.screen.blit(x_score_text, (10, screen_height - 90))
        self.screen.blit(o_score_text, (screen_width - o_score_text.get_width() - 10, screen_height - 90))

        player_state_text = self.game_state_font.render(f"Player {self.box_states} turn", True,(0,0,0))

        if self.draw:
            draw_text = self.game_state_font.render(f"DRAW", True, (0, 0, 0))
            self.screen.blit(draw_text, (screen_width // 2 - 40, screen_height - 90))
            self.game_over()


        elif self.game_over_bool:
            win_text = self.game_state_font.render(f"Player {self.current_symbol} wins", True, (0, 0, 0))
            self.screen.blit(win_text, (screen_width // 2 - 85, screen_height - 90))
            self.game_over()

        else:
            if self.x_turn:
                player_state_text = self.game_state_font.render(f"Player X turn", True, (0, 0, 0))
            else:
                player_state_text = self.game_state_font.render(f"Player O turn", True, (0, 0, 0))
            self.screen.blit(player_state_text, (screen_width // 2 - 85, screen_height - 90))

    def update_score(self):
        if self.current_symbol == "X":
            self.x_score += 1
        elif self.current_symbol == "O":
            self.o_score += 1

    def draw_boxes(self):
        for box in [self.box1, self.box2, self.box3, self.box4, self.box5, self.box6, self.box7, self.box8, self.box9]:
            pygame.draw.rect(self.screen, (255, 255, 255), box, 3)

    def activate_box(self):
        a, b = pygame.mouse.get_pos()
        for box in [self.box1, self.box2, self.box3, self.box4, self.box5, self.box6, self.box7, self.box8, self.box9]:
            box_x, box_y, box_w, box_h = box
            if box_x <= a <= box_x + box_w and box_y <= b <= box_y + box_h:
                pygame.draw.rect(self.screen, (180, 180, 180), box)

    def is_pressed_function(self, event):
        a, b = pygame.mouse.get_pos()
        for i, box in enumerate([self.box1, self.box2, self.box3, self.box4, self.box5, self.box6, self.box7, self.box8, self.box9]):
            box_rect = pygame.Rect(box)
            if event.type == pygame.MOUSEBUTTONDOWN and box_rect.collidepoint(a, b) and self.box_states[i] is None:
                if self.x_turn:
                    self.color_to_use = (255,0,0)
                    self.current_symbol = "X"
                    self.box_states[i] = 'X'
                    self.update_backend(i, 'x')
                else:
                    self.color_to_use = (0, 0, 255)
                    self.current_symbol = "O"
                    self.box_states[i] = 'O'
                    self.update_backend(i, 'o')
                self.x_turn = not self.x_turn  # Switch turn
                self.check_winner()

    def draw_on_the_boxes(self):
        for i, box in enumerate([self.box1, self.box2, self.box3, self.box4, self.box5, self.box6, self.box7, self.box8, self.box9]):
            if self.box_states[i] is not None:
                if self.box_states[i] == 'X':
                    color = (255, 0, 0)  # Red for 'X'
                else:
                    color = (0, 0, 255)  # Blue f
                text_surface = self.font.render(self.box_states[i], True, color)
                # Calculate the center position for the text in the current box
                text_rect = text_surface.get_rect(center=(box[0] + box[2] // 2, box[1] + box[3] // 2))
                # Blit the text surface onto the screen at the calculated position
                self.screen.blit(text_surface, text_rect)


    def update_backend(self, box_index, symbol):
        row, col = divmod(box_index, 3)
        self.list_of_rows[row][col] = symbol
        self.print_board()

    def print_board(self):
        # Determine which player's turn it is
        if self.x_turn:
            player = '1'
            symbol = 'X'
        else:
            self.current_symbol = "O"
            player = '2'
            symbol = 'O'
        # Print which player made the move and what symbol they placed
        print("Player " + player + " placed " + symbol)
        # Loop through each row in the list of rows
        for row in self.list_of_rows:
            # Print the row
            print(row)

    def check_winner(self):
        if winner_for_row(self.row_1, self.row_2, self.row_3):
            self.game_over_bool = True
            print("Game over!")

        elif winner_for_columns(self.row_1, self.row_2, self.row_3):
            self.game_over_bool = True

            print("Game over!")

        elif winner_for_diagonal(self.row_1, self.row_2, self.row_3):
            self.game_over_bool = True
            print("Game over!")
        else:
            # Check for draw
            draw_detected = True  # Assume the game is a draw initially
            # Iterate through each row in the list of rows
            for row in self.list_of_rows:
                # Iterate through each cell in the current row
                for cell in row:
                    # Check if the current cell is a space
                    if cell == " ":
                        # If any cell is a space, the game is not a draw
                        draw_detected = False
                        # No need to check further, exit the inner loop
                        break
                # If draw_detected is already False, no need to check further, exit the outer loop
                if not draw_detected:
                    break

            # If draw_detected is still True, then all cells are occupied, and it is a draw
            if draw_detected:
                self.draw = True

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                quit()  #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.draw:
                    self.reset_game()
                else:
                    self.update_score()
                    self.reset_game()
            if event.type == pygame.QUIT:
                pygame.quit()


    def reset_game(self):
        self.box_states = [None] * 9
        self.row_1 = [" ", " ", " "]
        self.row_2 = [" ", " ", " "]
        self.row_3 = [" ", " ", " "]
        self.list_of_rows = [self.row_1, self.row_2, self.row_3]
        self.x_turn = True
        self.game_over_bool = False
        self.draw = False
        self.current_symbol = "X"


def winner_for_row(row_1, row_2, row_3):
    for row in [row_1, row_2, row_3]:
        if row[0] == row[1] == row[2] and row[0] != " ":
            print(f"Player {row[0]} wins!")
            return True
    return False

def winner_for_columns(row_1, row_2, row_3):
    for col in range(3):
        if row_1[col] == row_2[col] == row_3[col] and row_1[col] != " ":
            print(f"Player {row_1[col]} wins!")
            return True
    return False

def winner_for_diagonal(row_1, row_2, row_3):
    if row_1[0] == row_2[1] == row_3[2] and row_1[0] != " ":
        print(f"Player {row_1[0]} wins!")
        return True
    if row_1[2] == row_2[1] == row_3[0] and row_1[2] != " ":
        print(f"Player {row_1[2]} wins!")
        return True
    return False

g = Game()
g.main_loop()
