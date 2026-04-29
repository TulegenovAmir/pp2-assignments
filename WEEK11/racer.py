import pygame
import random

# инициализация pygame
pygame.init()

# размеры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# загрузка изображений
car_img = pygame.image.load("resources/carrr.png")
road_img = pygame.image.load("resources/road.png")
coin_img = pygame.image.load("resources/coin1.png")

# изменение размера изображений
car_img = pygame.transform.scale(car_img, (50, 80))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
coin_img = pygame.transform.scale(coin_img, (20, 20))

# начальная позиция машины
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 100
car_speed = 5

# список монет
coins = []

# таймер появления монет
coin_timer = 0

# счёт игрока
score = 0

# шрифт для текста
font = pygame.font.SysFont(None, 30)

running = True

while running:

    # фон (дорога)
    screen.blit(road_img, (0, 0))

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление машиной
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # ограничение по экрану
    if car_x < 0:
        car_x = 0
    if car_x > WIDTH - 50:
        car_x = WIDTH - 50

    # увеличение таймера спавна монет
    coin_timer += 1

    # скорость появления монет (ускоряется при росте счёта)
    spawn_rate = 60
    if score > 10:
        spawn_rate = 40

    # создание монет
    if coin_timer > spawn_rate:
        coin_x = random.randint(20, WIDTH - 20)

        # вес монеты (разные значения очков)
        weight = random.choice([1, 2, 5])

        coins.append([coin_x, 0, weight])
        coin_timer = 0

    # движение монет вниз
    for coin in coins:
        coin[1] += 5

    # проверка столкновения с машиной
    for coin in coins[:]:
        if (car_x < coin[0] < car_x + 50) and (car_y < coin[1] < car_y + 80):
            coins.remove(coin)
            score += coin[2]  # добавляем вес монеты

    # удаление монет за пределами экрана
    coins = [c for c in coins if c[1] < HEIGHT]

    # рисование машины
    screen.blit(car_img, (car_x, car_y))

    # рисование монет
    for coin in coins:
        screen.blit(coin_img, (coin[0], coin[1]))

    # вывод счёта
    text = font.render(f"Coins: {score}", True, (0, 0, 0))
    screen.blit(text, (250, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()