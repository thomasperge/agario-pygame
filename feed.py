import random

class Feed :
    def __init__(self, name):
        self.nom = name
        self.x = 0
        self.y = 0

    def get_name(self):
        return self.nom
    
    def generated_random_position(self, screen_width, screen_height):
        self.x = random.randint(1, screen_width)
        self.y = random.randint(1, screen_height)
        return self.x, self.y

    def get_positions(self):
        return self.x, self.y
    
    def create_feed(self, screen_width, screen_height):
        self.x, self.y = self.generated_random_position(screen_width, screen_height)