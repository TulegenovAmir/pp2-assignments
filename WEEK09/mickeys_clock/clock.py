import pygame
import datetime

class Clock:
    def __init__(self):
        # загружаем изображение руки
        self.image = pygame.image.load("images/mickeyclock.png")
        self.image = pygame.transform.scale(self.image, (350, 250))

        # центр часов
        self.center = (300, 200)

    def draw(self, screen):
        now = datetime.datetime.now()

        seconds = now.second
        minutes = now.minute

        # ⏱ углы вращения
        sec_angle = -seconds * 6
        min_angle = -minutes * 6

        # вращаем руки
        sec_hand = pygame.transform.rotate(self.image, sec_angle)
        min_hand = pygame.transform.rotate(self.image, min_angle)

        # центрируем
        sec_rect = sec_hand.get_rect(center=self.center)
        min_rect = min_hand.get_rect(center=self.center)

        # рисуем
        screen.blit(sec_hand, sec_rect)
        screen.blit(min_hand, min_rect)