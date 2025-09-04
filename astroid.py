import circleshape as cs
import pygame
from constants import *
import random

class Asteroid(cs.CircleShape):

    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            v1 = pygame.math.Vector2.rotate_rad(self.velocity, angle)  
            v2 = pygame.math.Vector2.rotate_rad(self.velocity, -angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astr_1 = Asteroid(self.position[0], self.position[1], new_radius)
            astr_2 = Asteroid(self.position[0], self.position[1], new_radius)
            astr_1.velocity = v1*1.2
            astr_2.velocity = v2*1.2