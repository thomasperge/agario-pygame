class Player :
    def __init__(self, name, x, y, speed, size):
        self.nom = name
        self.xposition = x
        self.yposition = y
        self.speed = speed
        self.size = size
        self.direction = (self.speed, 0)

    def get_name(self):
        return self.nom
		
    def change_direction(self, x, y):
        self.direction = (x, y)

    def mouse_move(self, mouse_x, mouse_y):
        dx = mouse_x - self.get_position()[0]
        dy = mouse_y - self.get_position()[1]

        length = (dx ** 2 + dy ** 2) ** 0.5
        if length != 0:
            dx /= length
            dy /= length

        vx = dx * self.get_speed()
        vy = dy * self.get_speed()
        return vx, vy

    def move(self):
        self.xposition += self.direction[0]
        self.yposition += self.direction[1]

    def get_position(self):
        return self.xposition, self.yposition
    
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed
    
    def set_size(self, size):
        self.size = size
    
    def get_size(self):
        return self.size