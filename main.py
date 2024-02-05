import pygame

# Screen
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
background = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
screen.fill(background)

game_started = True
clock = pygame.time.Clock()

while game_started :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_started = False

pygame.quit()