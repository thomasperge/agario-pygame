import pygame
from player import Player
from feed import Feed

# Screen
pygame.init()
width = 1125
height = 675
screen = pygame.display.set_mode((width, height))
background = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
screen.fill(background)

# Inititalize Player
player = Player("Player1", 300, 300, 3)

# Initialize Feed1
feed1 = Feed("Feed1")

# Display Player Sprite
playerSprite = pygame.Rect(0, 0, 25, 25)
playerSprite.x = player.get_position()[0]
playerSprite.y = player.get_position()[1]

# Display Feed Sprite
feed1Sprite = pygame.Rect(0, 0, 25, 25)
feed1.display_feed(width, height, feed1Sprite)

pygame.draw.rect(screen, blue, playerSprite)
pygame.draw.rect(screen, red, feed1Sprite)

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
    mouse_position = player.mouse_move(mouse_x, mouse_y)
    player.change_direction(mouse_position[0], mouse_position[1])

    # Display new sprite
    playerSprite.x = player.get_position()[0]
    playerSprite.y = player.get_position()[1]
    player.move()

    screen.fill(background)
    pygame.draw.rect(screen, blue, playerSprite)
    pygame.draw.rect(screen, red, feed1Sprite)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()