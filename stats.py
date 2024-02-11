import pygame
import sys
from button import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Stats:
    def __init__(self, screen, menu_class, score):
        self.screen = screen
        self.menu_class = menu_class
        self.score = score
        self.back_to_menu = Button("Back to Menu", (self.screen.get_width() // 2, 350), "menu", None)

        pygame.display.set_caption("Game - Stats")

    def draw(self):
        self.screen.fill(WHITE)

        # Draw all title
        title_font = pygame.font.Font(None, 40)
        score_font = pygame.font.Font(None, 30)
        title_text = title_font.render("Game Finish !", True, BLACK)
        score_text = score_font.render("Final Score: {}".format(self.score), True, BLACK)
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 200))
        score_rect = score_text.get_rect(center=(self.screen.get_width() // 2, 250))
        self.screen.blit(title_text, title_rect)
        self.screen.blit(score_text, score_rect)

        self.back_to_menu.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.back_to_menu.rect.collidepoint(event.pos):
                        self.menu_class.run()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
