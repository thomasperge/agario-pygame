import pygame
from player import Player
from feed import Feed
from trap import Trap

class Game:
    def __init__(self):
        pygame.init()

        self.width = 1125
        self.height = 675
        self.background = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.clock = pygame.time.Clock()

        self.feeds = [Feed("Feed1", 9), Feed("Feed2", 9), Feed("Feed3", 9), Feed("Feed4", 9), Feed("Feed5", 9)]
        self.traps = [Trap("Trap1", 40, 150), Trap("Trap2", 40, 150)]
        self.player = Player("Player1", 300, 300, 4, 75)

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.background)

    def create_sprite(self):
        for feed in self.feeds:
            feed.create_feed(self.width, self.height)

        for trap in self.traps:
            trap.create_trap(self.width, self.height)

    def lauch_game(self, is_launched, is_played_with_mouse):
        self.create_sprite()

        while is_launched:
            # Leave the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_launched = False
                    
            # Mouse
            if is_played_with_mouse:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                player_x, player_y = self.player.get_position()

                if (player_x - self.player.get_size() / (self.player.get_size() - 2) < mouse_x < player_x + self.player.get_size() / (self.player.get_size() - 2)) and (player_y - self.player.get_size() / (self.player.get_size() - 2) < mouse_y < player_y + self.player.get_size() / (self.player.get_size() - 2)):
                    self.player.change_direction(0, 0)
                else:
                    mouse_position = self.player.mouse_move(mouse_x, mouse_y)
                    self.player.change_direction(int(mouse_position[0]), int(mouse_position[1]))
            # Keyboard
            else :
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            self.player.change_direction(0, self.player.get_speed())
                        elif event.key == pygame.K_UP:
                            self.player.change_direction(0, -self.player.get_speed())
                        elif event.key == pygame.K_RIGHT:
                            self.player.change_direction(self.player.get_speed(), 0)
                        elif event.key == pygame.K_LEFT:
                            self.player.change_direction(-self.player.get_speed(), 0)

            # == Collision ==
            # Check if player is out of screen boundaries
            if player_x - self.player.get_size() / 2 < 0:
                self.player.set_position(self.width - self.player.get_size() / 2, player_y)
            elif player_x + self.player.get_size() / 2 > self.width:
                self.player.set_position(self.player.get_size() / 2, player_y)
            elif player_y - self.player.get_size() / 2 < 0:
                self.player.set_position(player_x, self.height - self.player.get_size() / 2)
            elif player_y + self.player.get_size() / 2 > self.height:
                self.player.set_position(player_x, self.player.get_size() / 2)

            # Collision with feed(s)
            for feed in self.feeds:
                distance = ((self.player.get_position()[0] - feed.get_position()[0]) ** 2 + (self.player.get_position()[1] - feed.get_position()[1]) ** 2) ** 0.5

                if distance <= self.player.get_size() + feed.get_size():
                    self.player.set_size(self.player.get_size() + 2)
                    # player.set_speed(player.get_speed() + 5)
                    self.feeds.remove(feed)

                    # Create new feed
                    new_feed_name = "Feed" + str(len(self.feeds) + 1)
                    newfeed = Feed(new_feed_name, 9)
                    newfeed.create_feed(self.width, self.height)
                    self.feeds.append(newfeed)

            # Collision with traps(s)
            for trap in self.traps:
                distance = ((self.player.get_position()[0] - trap.get_position()[0]) ** 2 + (self.player.get_position()[1] - trap.get_position()[1]) ** 2) ** 0.5

                if distance <= self.player.get_size() + trap.get_size():
                    if self.player.get_size() > trap.get_size():
                        self.player.set_size(self.player.get_size() / 2)
                        self.traps.remove(trap)

                        # Create new Trap
                        new_trap_name = "Trap" + str(len(self.traps) + 1)
                        newTrap = Trap(new_trap_name, 40, 150)
                        newTrap.create_trap(self.width, self.height)
                        self.traps.append(newTrap)

            # == Draw / Display ==
            # Move player
            self.player.move()
            self.screen.fill(self.background)

            # Display Player
            pygame.draw.circle(self.screen, self.blue, self.player.get_position(), self.player.get_size())

            # Display all feeds
            for feed in self.feeds:
                pygame.draw.circle(self.screen, self.green, feed.get_position(), feed.get_size())

            # Display all traps
            for trap in self.traps:
                pygame.draw.circle(self.screen, self.red, trap.get_position(), trap.get_size())

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()