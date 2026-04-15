import pygame
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Moving Ball")

ball = Ball()
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball.move(keys)

    screen.fill((255, 255, 255))
    ball.draw(screen)

    pygame.display.flip()

pygame.quit()