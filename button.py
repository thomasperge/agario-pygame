import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HOVER_COLOR = (100, 100, 255)

class Button:
    def __init__(self, text, position, value, group):
        self.text = text
        self.position = position
        self.value = value
        self.group = group
        self.font = pygame.font.Font(None, 36)
        self.surface = self.font.render(text, True, BLACK)
        self.rect = self.surface.get_rect(center=position)
        self.selected = False

    def draw(self, screen):
        color = HOVER_COLOR if self.selected else BLACK
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            color = HOVER_COLOR
            
        self.surface = self.font.render(self.text, True, color)
        screen.blit(self.surface, self.rect)

    def reset_colors(self):
        self.selected = False

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)