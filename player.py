class Player :
    def __init__(self, name, x, y, speed):
        self.nom = name
        self.xposition = x
        self.yposition = y
        self.speed = speed
        self.direction = (self.speed, 0)

    def get_name(self):
        return self.nom
		
    def change_direction(self, x, y):
        self.direction = (x, y)

    def move(self):
        self.xposition += self.direction[0]
        self.yposition += self.direction[1]

    def get_position(self):
        return self.xposition, self.yposition
    
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed