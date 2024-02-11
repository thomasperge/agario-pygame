import pygame
import sys
from button import Button
from game import Game

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
HOVER_COLOR = (100, 100, 255)

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.difficulty_buttons = []
        self.difficulty = None
        self.game_handle = None
        self.create_buttons()

        pygame.display.set_caption("Menu")
    
    def create_buttons(self):
        # Initialize all buttons
        play_keyboard_button = Button("Play with keyboard", (self.screen.get_width() // 2, 200), "keyboard", "play")
        play_mouse_button = Button("Play with mouse", (self.screen.get_width() // 2, 250), "mouse", "play")
        quit_button = Button("Quit (Q)", (self.screen.get_width() // 2, 300), "quit", None)
        self.buttons = [play_keyboard_button, play_mouse_button, quit_button]

        difficulties = ["Facile", "Normal", "Difficile"]
        for i, diff in enumerate(difficulties):
            diff_button = Button(diff, (self.screen.get_width() // 2 + (i - 1) * 150, 435), diff.lower(), "difficulty")
            self.difficulty_buttons.append(diff_button)


    def draw(self):
        self.screen.fill(WHITE)

        # Title
        big_title_font = pygame.font.Font(None, 50)
        big_title_text = big_title_font.render("Agario Pygame", True, RED)
        big_title_rect = big_title_text.get_rect(center=(self.screen.get_width() // 2, 100))

        # Draw all button
        title_font = pygame.font.Font(None, 36)
        title_text = title_font.render("Choose Difficulty:", True, GREEN)
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 390))
        self.screen.blit(title_text, title_rect)
        self.screen.blit(big_title_text, big_title_rect)

        for button in self.buttons:
            button.draw(self.screen)

        for button in self.difficulty_buttons:
            button.draw(self.screen)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # == Menu Event ==
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons + self.difficulty_buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        # Difficulty
                        if button.group == "difficulty":
                            for btn in self.difficulty_buttons:
                                btn.selected = False
                            button.selected = True
                            self.difficulty = button.value
                            print("Selected difficulty:", button.value)
                        # Type (Mouse/Key)
                        elif button.group == "play":
                            for btn in self.buttons:
                                btn.selected = False
                            button.selected = True
                            self.game_handle = button.value
                            print("Selected play option:", button.value)
                        # Quit
                        elif button.value == "quit":
                            pygame.quit()
                            sys.exit()

            # Keyboard input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_P:
                    # Set game handle to keyboard
                    for btn in self.buttons:
                        btn.selected = False
                    self.game_handle = "keyboard"
                    print("Selected play option: keyboard")

    def game_settings(self):
        data = [None, None]
        if self.game_handle == "mouse":
            data[0] = True
        else:
            data[0] = False

        if self.difficulty == "facile":
            data[1] = 2
        elif self.difficulty == "normal":
            data[1] = 3
        elif self.difficulty == "difficile":
            data[1] = 4

        return data
    
    def reset_settings(self):
        for button in self.buttons:
            button.reset_colors()

        for button in self.difficulty_buttons:
            button.reset_colors()

        self.game_handle = None
        self.difficulty = None
    
    def run(self):
        game_launched = False
        while not game_launched:
            self.handle_events()
            self.draw()

            if not game_launched and self.game_handle is not None and self.difficulty is not None:
                game = Game(self.screen, self.game_settings()[0], self.game_settings()[1], self)
                game.run(True)
                game_launched = True

        pygame.quit()
        sys.exit()
