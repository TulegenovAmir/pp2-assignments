import pygame
import sys
import random
from config import *
from db import init_db, get_top_scores
from game import run_game

# запускаем pygame
pygame.init()

# создаём окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS4: Snake Database Edition")

# шрифты
font_main = pygame.font.SysFont("Verdana", 24)
font_big = pygame.font.SysFont("Verdana", 48, bold=True)
font_small = pygame.font.SysFont("Verdana", 18)

# кнопка для меню
class Button:
    def __init__(self, x, y, w, h, text, color=GRAY):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self, surface):
        # рисуем кнопку
        pygame.draw.rect(surface, self.color, self.rect, border_radius=5)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=5)

        # пишем текст
        txt_img = font_main.render(self.text, True, WHITE)
        surface.blit(txt_img, txt_img.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        # проверка клика мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False


# просто вывод текста по центру
def draw_text(text, font, color, y_pos):
    img = font.render(text, True, color)
    screen.blit(img, img.get_rect(center=(WIDTH // 2, y_pos)))


# ввод имени игрока
def ask_username():
    username = ""

    while True:
        screen.fill(BLACK)
        draw_text("ENTER NAME", font_main, GREEN, 200)

        # поле ввода
        pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 150, 250, 300, 50))
        draw_text(username + "|", font_main, YELLOW, 275)

        draw_text("Press ENTER", font_small, WHITE, 350)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:

                # enter = начать
                if event.key == pygame.K_RETURN and username:
                    return username

                # удалить букву
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                # добавляем буквы
                elif len(username) < 15:
                    username += event.unicode


# главное меню
def main_menu():

    btn_play = Button(200, 200, 200, 50, "PLAY", GREEN)
    btn_leader = Button(200, 270, 200, 50, "LEADERBOARD")
    btn_settings = Button(200, 340, 200, 50, "SETTINGS")
    btn_quit = Button(200, 410, 200, 50, "QUIT", RED)

    while True:
        screen.fill(BLACK)
        draw_text("SNAKE GAME", font_big, WHITE, 100)

        for b in [btn_play, btn_leader, btn_settings, btn_quit]:
            b.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if btn_quit.is_clicked(event):
                return "quit"

            if btn_play.is_clicked(event):
                return "play"

            if btn_leader.is_clicked(event):
                return "leaderboard"

            if btn_settings.is_clicked(event):
                return "settings"


# таблица рекордов
def leaderboard_screen():

    scores = get_top_scores()

    btn_back = Button(200, 520, 200, 40, "BACK")

    while True:
        screen.fill(BLACK)
        draw_text("TOP PLAYERS", font_main, YELLOW, 50)

        y = 120

        # выводим игроков
        for i, (name, score, lvl, date) in enumerate(scores):
            text = f"{i+1}. {name} | {score} | lvl {lvl}"
            draw_text(text, font_small, WHITE, y)
            y += 35

        btn_back.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if btn_back.is_clicked(event):
                return "menu"


# настройки
def settings_screen():

    current = load_settings()

    btn_grid = Button(150, 200, 300, 50, f"GRID: {'ON' if current['grid'] else 'OFF'}")
    btn_color = Button(150, 270, 300, 50, "CHANGE COLOR")
    btn_back = Button(200, 400, 200, 50, "SAVE & BACK", GREEN)

    while True:
        screen.fill(BLACK)

        draw_text("SETTINGS", font_main, BLUE, 100)

        # цвет змейки
        pygame.draw.rect(screen, current['snake_color'], (WIDTH//2 - 25, 330, 50, 50))

        for b in [btn_grid, btn_color, btn_back]:
            b.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            # вкл/выкл сетку
            if btn_grid.is_clicked(event):
                current['grid'] = not current['grid']
                btn_grid.text = f"GRID: {'ON' if current['grid'] else 'OFF'}"

            # меняем цвет
            if btn_color.is_clicked(event):
                current['snake_color'] = [random.randint(50, 255) for _ in range(3)]

            # сохраняем
            if btn_back.is_clicked(event):
                save_settings(current)
                return "menu"


# game over экран
def game_over_screen(res):

    btn_retry = Button(100, 400, 180, 50, "RETRY", GREEN)
    btn_menu = Button(320, 400, 180, 50, "MENU")

    while True:
        screen.fill(BLACK)

        draw_text("GAME OVER", font_big, RED, 150)

        # результат
        draw_text(f"SCORE: {res['score']}", font_main, WHITE, 230)
        draw_text(f"LEVEL: {res['level']}", font_main, WHITE, 270)
        draw_text(f"BEST: {res['best']}", font_main, YELLOW, 320)

        btn_retry.draw(screen)
        btn_menu.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if btn_retry.is_clicked(event):
                return "retry"

            if btn_menu.is_clicked(event):
                return "menu"


# главная функция
def main():

    # создаём базу
    try:
        init_db()
    except Exception as e:
        print("DB error:", e)

    while True:

        state = main_menu()

        if state == "quit":
            break

        elif state == "leaderboard":
            leaderboard_screen()

        elif state == "settings":
            settings_screen()

        elif state == "play":

            # ввод имени
            user = ask_username()
            if not user:
                continue

            # игра
            while True:

                game_state, result = run_game(screen, user, load_settings())

                if game_state == "quit":
                    pygame.quit()
                    sys.exit()

                action = game_over_screen(result)

                if action == "retry":
                    continue

                break

    pygame.quit()


# запуск
if __name__ == "__main__":
    main()