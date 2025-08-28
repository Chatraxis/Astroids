import circleshape as cs
from constants import *



class Player(cs.CircleShape):
    def __init__(self, x, y):
        self.__x_pos = x
        self.__y_pos = y 
        super().__init__(radius=PLAYER_RADIUS)
        rotation = 0


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    