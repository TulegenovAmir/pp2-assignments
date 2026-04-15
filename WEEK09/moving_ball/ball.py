import pygame

class Ball:
    def __init__(self):
        self.x = 300
        self.y = 200
        self.radius = 25
        self.speed = 20

    def move(self, keys):
        if keys[pygame.K_UP] and self.y - self.speed - self.radius >= 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.speed + self.radius <= 400:
            self.y += self.speed
        if keys[pygame.K_LEFT] and self.x - self.speed - self.radius >= 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.speed + self.radius <= 600:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)