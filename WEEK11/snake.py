import pygame
import random
import time

# инициализация pygame
pygame.init()

# размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# цвета
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# размер блока змейки
block_size = 20

# начальное положение змейки
snake = [(100, 100)]

# направление движения
direction = (block_size, 0)

# функция создания еды
def spawn_food():
    x = random.randrange(0, WIDTH, block_size)
    y = random.randrange(0, HEIGHT, block_size)

    # вес еды (сколько даёт очков)
    weight = random.choice([1, 2, 3])

    return (x, y, weight)

# первая еда
food = spawn_food()

# время появления еды
food_time = time.time()

# время жизни еды (секунды)
food_lifetime = 5

# счёт игрока
score = 0

# уровень игры
level = 1

# скорость игры
speed = 10

# шрифт
font = pygame.font.SysFont(None, 30)

running = True

while running:

    # фон
    screen.fill(WHITE)

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # управление стрелками
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -block_size)
            if event.key == pygame.K_DOWN:
                direction = (0, block_size)
            if event.key == pygame.K_LEFT:
                direction = (-block_size, 0)
            if event.key == pygame.K_RIGHT:
                direction = (block_size, 0)

    # новая голова змейки
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # проверка выхода за границы
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False

    # проверка столкновения с собой
    if new_head in snake:
        running = False

    # добавляем новую голову
    snake.insert(0, new_head)

    # проверка времени жизни еды
    if time.time() - food_time > food_lifetime:
        food = spawn_food()
        food_time = time.time()

    # проверка поедания еды
    if new_head == (food[0], food[1]):
        score += food[2]  # добавляем вес еды
        food = spawn_food()
        food_time = time.time()

        # повышение уровня каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        # если не съели — убираем хвост
        snake.pop()

    # рисуем змейку
    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, block_size, block_size))

    # рисуем еду
    pygame.draw.rect(screen, RED, (food[0], food[1], block_size, block_size))

    # вывод текста
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 40))

    # обновление экрана
    pygame.display.update()

    # FPS / скорость игры
    clock.tick(speed)

pygame.quit()