import pygame
from player import Player
from feed import Feed
from trap import Trap
from stats import Stats

BACKGROUND = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Game:
    def __init__(self, screen, is_played_with_mouse, difficulty, menu_class):
        self.menu_class = menu_class
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.difficulty = difficulty
        self.is_played_with_mouse = is_played_with_mouse

        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
        self.score = 0

        if difficulty == 2:
            num_traps = 2
            num_feeds = 5
        elif difficulty == 3:
            num_traps = 3
            num_feeds = 3
        elif difficulty == 4:
            num_traps = 4
            num_feeds = 2

        self.traps = [Trap(f"Trap{i+1}", 40, 150) for i in range(num_traps)]
        self.feeds = [Feed(f"Feed{i+1}", 9) for i in range(num_feeds)]
        self.player = Player("Player1", 300, 300, 4, 75)

        self.screen = screen
        pygame.display.set_caption("Game")
        self.font = pygame.font.Font(None, 36)
        self.create_sprite()

    def create_sprite(self):
        for feed in self.feeds:
            feed.create_feed(self.width, self.height)

        for trap in self.traps:
            trap.create_trap(self.width, self.height)

    def run(self, is_launched):
        while is_launched:
            # Leave the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_launched = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        self.menu_class.reset_settings()
                        self.menu_class.run()

            player_x, player_y = self.player.get_position()
    
            # Mouse
            if self.is_played_with_mouse:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (player_x - self.player.get_size() / (self.player.get_size() - 2) < mouse_x < player_x + self.player.get_size() / (self.player.get_size() - 2)) and (player_y - self.player.get_size() / (self.player.get_size() - 2) < mouse_y < player_y + self.player.get_size() / (self.player.get_size() - 2)):
                    self.player.change_direction(0, 0)
                else:
                    mouse_position = self.player.mouse_move(mouse_x, mouse_y)
                    self.player.change_direction(int(mouse_position[0]), int(mouse_position[1]))
            # Keyboard
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    self.player.change_direction(0, self.player.get_speed())
                elif keys[pygame.K_z]:
                    self.player.change_direction(0, -self.player.get_speed())
                elif keys[pygame.K_d]:
                    self.player.change_direction(self.player.get_speed(), 0)
                elif keys[pygame.K_q]:
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
                    if self.player.get_size() < 150 :
                        self.player.set_size(self.player.get_size() + 2)

                    if self.player.get_speed() < 11 :
                        self.player.set_speed(self.player.get_speed() + 0.5)

                    self.feeds.remove(feed)
                    self.score += 1

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
                        self.player.set_speed(self.player.get_speed() / self.difficulty)
                        self.traps.remove(trap)

                        # Create new Trap
                        new_trap_name = "Trap" + str(len(self.traps) + 1)
                        newTrap = Trap(new_trap_name, 40, 150)
                        newTrap.create_trap(self.width, self.height)
                        self.traps.append(newTrap)

            # == Draw / Display & Score / Timer==
            # Timer
            elapsed_time = pygame.time.get_ticks() - self.start_time
            remaining_seconds = max(60 - elapsed_time // 1000, 0)

            if remaining_seconds == 0:
                self.menu_class.reset_settings()

                stats = Stats(self.screen, self.menu_class, self.score)
                stats.run()

            # Move all sprite
            self.player.move()
            self.screen.fill(BACKGROUND)

            pygame.draw.circle(self.screen, BLUE, self.player.get_position(), self.player.get_size())

            for trap in self.traps:
                pygame.draw.circle(self.screen, RED, trap.get_position(), trap.get_size())
                
            for feed in self.feeds:
                pygame.draw.circle(self.screen, GREEN, feed.get_position(), feed.get_size())

            timer_text = self.font.render("Time: {} s".format(remaining_seconds), True, (0, 0, 0))
            score_text = self.font.render("Score: {}".format(self.score), True, (0, 0, 0))
            speed_text = self.font.render("Speed: {} km/h".format(self.player.speed), True, (0, 0, 0))
            size_text = self.font.render("Size: {}".format(self.player.size), True, (0, 0, 0))
            difficulty_text = self.font.render("Difficulty: {}".format(self.difficulty), True, (0, 0, 0))
            self.screen.blit(timer_text, (10, 10))
            self.screen.blit(score_text, (10, 40))
            self.screen.blit(speed_text, (10, 70))
            self.screen.blit(size_text, (10, 100))
            self.screen.blit(difficulty_text, (10, 130))

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()