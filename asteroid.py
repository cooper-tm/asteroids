import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random.uniform(20, 50)
        a_vector = self.velocity.rotate(self.rotation)
        b_vector = self.velocity.rotate(-self.rotation)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_a1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_a2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_a1.velocity = a_vector * 1.2
        new_a2.velocity = b_vector * 1.2
