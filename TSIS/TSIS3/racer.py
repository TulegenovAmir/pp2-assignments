import pygame
import random
import os

# полосы дороги (3 линии где может ехать игрок)
LANES = [200, 300, 400]

# базовая скорость
SPEED_BASE = 5


# загрузка картинок
def load_image(name, width, height):

    path = os.path.join('assets', 'images', name)

    try:
        # если файл есть — грузим картинку
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (width, height))

    except FileNotFoundError:
        # если нет картинки — делаем цветной квадрат
        surf = pygame.Surface((width, height))
        surf.fill((255, 0, 255))
        return surf


# игрок
class Player(pygame.sprite.Sprite):

    def __init__(self, color_name):
        super().__init__()

        # картинка игрока
        filename = f"player_{color_name}.png"
        self.image = load_image(filename, 40, 70)

        # стартовая позиция
        self.rect = self.image.get_rect(center=(300, 500))

        self.speed = 6

        # бонусы
        self.shield_active = False
        self.nitro_active = False

        self.powerup_timer = 0

        # сколько ошибок можно простить
        self.crashes_allowed = 0

    def update(self):

        keys = pygame.key.get_pressed()

        # скорость (если нитро — быстрее)
        current_speed = self.speed * 1.5 if self.nitro_active else self.speed

        # движение влево / вправо
        if keys[pygame.K_LEFT] and self.rect.left > 150:
            self.rect.x -= current_speed

        if keys[pygame.K_RIGHT] and self.rect.right < 450:
            self.rect.x += current_speed

        # движение вверх / вниз (немного быстрее/медленнее)
        if keys[pygame.K_UP] and self.rect.top > 50:
            self.rect.y -= current_speed / 2

        if keys[pygame.K_DOWN] and self.rect.bottom < 580:
            self.rect.y += current_speed / 2

        # выключаем бонусы по времени
        if (self.nitro_active or self.shield_active) and pygame.time.get_ticks() > self.powerup_timer:
            self.nitro_active = False
            self.shield_active = False


# враги
class Enemy(pygame.sprite.Sprite):

    def __init__(self, difficulty):
        super().__init__()

        self.image = load_image("enemy.png", 40, 70)

        self.rect = self.image.get_rect(center=(random.choice(LANES), -100))

        # скорость зависит от сложности
        self.speed = SPEED_BASE + (2 if difficulty == "hard" else 0)

    def update(self):
        # движение вниз
        self.rect.y += self.speed

        # если вышел за экран — удаляем
        if self.rect.top > 600:
            self.kill()


# препятствия
class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = load_image("obstacle.png", 40, 40)

        self.rect = self.image.get_rect(center=(random.choice(LANES), -50))

    def update(self):

        self.rect.y += SPEED_BASE

        if self.rect.top > 600:
            self.kill()


# бонусы
class PowerUp(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # случайный тип бонуса
        self.type = random.choice(["Nitro", "Shield", "Repair"])

        img_name = self.type.lower() + ".png"
        self.image = load_image(img_name, 30, 30)

        self.rect = self.image.get_rect(center=(random.choice(LANES), -50))

        self.speed = SPEED_BASE

    def update(self):

        self.rect.y += self.speed

        if self.rect.top > 600:
            self.kill()


# монетки
class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # шанс монет: 1 / 2 / 5 очков
        r = random.random()

        if r < 0.7:
            self.value = 1
        elif r < 0.9:
            self.value = 2
        else:
            self.value = 5

        # создаём кружок вместо картинки
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)

        # цвет монеты
        if self.value == 1:
            color = (255, 215, 0)
        elif self.value == 2:
            color = (0, 255, 0)
        else:
            color = (255, 0, 255)

        pygame.draw.circle(self.image, color, (10, 10), 10)

        # позиция появления
        self.rect = self.image.get_rect(center=(random.choice(LANES), -30))

        self.speed = SPEED_BASE

    def update(self):

        self.rect.y += self.speed

        if self.rect.top > 600:
            self.kill()