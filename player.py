import circleshape as cs
from constants import *
import pygame
from shot import *

class Player(cs.CircleShape):
    
    containers = ()

    def __init__(self, x, y, radius = PLAYER_RADIUS, rotation = 0, timer = 0):
        self.__x_pos = x
        self.__y_pos = y 
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.timer = timer

    
        

    

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]  
                                                    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            dt_m = float(0-dt)
            self.rotate(dt_m)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:       
            dt_m = float(0-dt)
            self.move(dt_m)
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                pass
            else:
                self.shot(dt)
                self.timer = PLAYER_SHOOT_COOLDOWN


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shot(self, dt):
        bullet = Shot(self.position[0] , self.position[1], SHOT_RADIUS)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        
        bullet.velocity += direction * PLAYER_SHOT_SPEED 
    
        
    
