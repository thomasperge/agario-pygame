import pygame
from player import Player
from feed import Feed
from trap import Trap

# Init Screen
pygame.init()
width = 1125
height = 675
screen = pygame.display.set_mode((width, height))
background = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
screen.fill(background)

# Inititalize Player
player = Player("Player1", 300, 300, 4, 75)

# Initialize Feed1
feed1 = Feed("Feed1", 9)
feed2 = Feed("Feed2", 9)
feed3 = Feed("Feed3", 9)
feed4 = Feed("Feed4", 9)
feed5 = Feed("Feed5", 9)

# Initialize Feed1
trap1 = Trap("Trap1", 40, 150)
trap2 = Trap("Feed2", 40, 150)

feeds = [feed1, feed2, feed3, feed4, feed5]
traps = [trap1, trap2]

feed1.create_feed(width, height)
feed2.create_feed(width, height)
feed3.create_feed(width, height)
feed4.create_feed(width, height)
feed5.create_feed(width, height)

trap1.create_trap(width, height)
trap2.create_trap(width, height)

game_started = True
clock = pygame.time.Clock()

while game_started:
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
    player_x, player_y = player.get_position()

    if (player_x - player.get_size() / (player.get_size() - 2) < mouse_x < player_x + player.get_size() / (player.get_size() - 2)) and (player_y - player.get_size() / (player.get_size() - 2) < mouse_y < player_y + player.get_size() / (player.get_size() - 2)):
        player.change_direction(0, 0)
    else:
        mouse_position = player.mouse_move(mouse_x, mouse_y)
        player.change_direction(int(mouse_position[0]), int(mouse_position[1]))

    # Collision with feed(s)
    for feed in feeds:
        distance = ((player.get_position()[0] - feed.get_position()[0]) ** 2 + (player.get_position()[1] - feed.get_position()[1]) ** 2) ** 0.5

        if distance <= player.get_size() + feed.get_size():
            player.set_size(player.get_size() + 2)
            # player.set_speed(player.get_speed() + 5)
            feeds.remove(feed)

            # Create new feed
            new_feed_name = "Feed" + str(len(feeds) + 1)
            newfeed = Feed(new_feed_name, 9)
            newfeed.create_feed(width, height)
            feeds.append(newfeed)

    # Collision with traps(s)
    for trap in traps:
        distance = ((player.get_position()[0] - trap.get_position()[0]) ** 2 + (player.get_position()[1] - trap.get_position()[1]) ** 2) ** 0.5

        if distance <= player.get_size() + trap.get_size():
            if player.get_size() > trap.get_size():
                player.set_size(player.get_size() / 2)
                traps.remove(trap)

                # Create new Trap
                new_trap_name = "Trap" + str(len(traps) + 1)
                newTrap = Trap(new_trap_name, 40, 150)
                newTrap.create_trap(width, height)
                traps.append(newTrap)

    # Move player
    player.move()

    screen.fill(background)

    # Display Player
    pygame.draw.circle(screen, blue, player.get_position(), player.get_size())

    # Display all feeds
    for feed in feeds:
        pygame.draw.circle(screen, green, feed.get_position(), feed.get_size())

     # Display all traps
    for trap in traps:
        pygame.draw.circle(screen, red, trap.get_position(), trap.get_size())

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
