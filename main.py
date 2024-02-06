import pygame
from player import Player

# Screen
pygame.init()
width = 1125
height = 675
screen = pygame.display.set_mode((width, height))
background = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
screen.fill(background)

# Inititalize Snake
player = Player("Gabriel_Le_Snake", 300, 300, 3)

# Display Snake Sprite
playerSprite = pygame.Rect(0, 0, 25, 25)
playerSprite.x = player.get_position()[0]
playerSprite.y = player.get_position()[1]

pygame.draw.rect(screen, blue, playerSprite)

game_started = True
clock = pygame.time.Clock()

while game_started :
    # Keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_started = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.change_direction(0, player.get_speed())
            elif event.key == pygame.K_UP:
                player.change_direction(0, -player.get_speed())
            elif event.key == pygame.K_RIGHT:
                player.change_direction(player.get_speed(), 0)
            elif event.key == pygame.K_LEFT:
                player.change_direction(-player.get_speed(), 0)
    
    # Mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculating direction vector
    dx = mouse_x - player.get_position()[0]
    dy = mouse_y - player.get_position()[1]

    # Normalizing the direction vector
    length = (dx ** 2 + dy ** 2) ** 0.5
    if length != 0:
        dx /= length
        dy /= length

    # Moving the player with normalized direction and constant speed
    vx = dx * player.get_speed()
    vy = dy * player.get_speed()

    player.change_direction(vx, vy)
    player.move()

    playerSprite.x = player.get_position()[0]
    playerSprite.y = player.get_position()[1]
    player.move()

    screen.fill(background)
    pygame.draw.rect(screen, blue, playerSprite)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()