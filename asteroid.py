import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            split_angle_1 = self.velocity.rotate(random_angle)
            split_angle_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_1 = Asteroid(self.position[0],self.position[1],new_radius)
            split_asteroid_1.velocity = split_angle_1*1.2
            split_asteroid_2 = Asteroid(self.position[0],self.position[1],new_radius)
            split_asteroid_2.velocity = split_angle_2*1.2