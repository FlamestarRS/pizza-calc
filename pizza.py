import pygame
import math
from circleshape import *


class Pizza(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 5)
        #self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def area(self, d):
        return math.pi * d
    
    def diameter(self, area):
        return area / math.pi
