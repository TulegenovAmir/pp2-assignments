import pygame
from clock import Clock

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Mickey Clock")

clock_obj = Clock()
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(1)  # обновление раз в секунду

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # белый фон

    clock_obj.draw(screen)

    pygame.display.flip()

pygame.quit()