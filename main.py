import pygame
from menu import Menu

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")
    menu = Menu(screen)
    menu.run()