import pygame
import sys
import math
import datetime


# размеры окна
SCREEN_W = 1000
SCREEN_H = 700

# ширина панели инструментов слева
TOOLBAR_W = 180

# область рисования
CANVAS_X = TOOLBAR_W
CANVAS_W = SCREEN_W - TOOLBAR_W
CANVAS_H = SCREEN_H


# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# фон панели и холста
BG_TOOLBAR = (33, 33, 33)
BG_CANVAS = (255, 255, 255)

# цвет выделения
HIGHLIGHT = (0, 120, 215)


# палитра цветов
PALETTE = [
    (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0),
    (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128),
    (0, 255, 255), (255, 0, 255), (165, 42, 42), (128, 128, 128)
]


# список инструментов
TOOL_PENCIL = "pencil"
TOOL_LINE = "line"
TOOL_RECT = "rect"
TOOL_SQUARE = "square"
TOOL_CIRCLE = "circle"
TOOL_RTRIANGLE = "right_tri"
TOOL_EQTRIANGLE = "eq_tri"
TOOL_RHOMBUS = "rhombus"
TOOL_FILL = "fill"
TOOL_TEXT = "text"
TOOL_ERASER = "eraser"


# функция загрузки картинки
def load_image(name, width, height):

    path = f"assets/images/{name}"

    try:
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (width, height))

    except FileNotFoundError:
        # если нет картинки — делаем заглушку
        surf = pygame.Surface((width, height))
        surf.fill((255, 0, 255))
        return surf


# функция заливки (bucket tool)
def flood_fill(surface, pos, fill_color):

    target_color = surface.get_at(pos)

    # если уже такой цвет — ничего не делаем
    if target_color == fill_color:
        return

    pixels = [pos]
    visited = set()

    w, h = surface.get_size()

    while pixels:
        x, y = pixels.pop()

        if (x, y) in visited:
            continue

        if x < 0 or x >= w or y < 0 or y >= h:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), fill_color)
        visited.add((x, y))

        pixels.extend([
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1)
        ])


# главный класс приложения
class PaintApp:

    def __init__(self):

        pygame.init()

        # окно
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption("Paint TSIS")

        self.clock = pygame.time.Clock()

        # шрифты
        self.font = pygame.font.SysFont("Arial", 16)
        self.text_font = pygame.font.SysFont("Verdana", 24)

        # холст (где рисуем)
        self.canvas = pygame.Surface((CANVAS_W, CANVAS_H))
        self.canvas.fill(BG_CANVAS)

        # текущий инструмент
        self.active_tool = TOOL_PENCIL

        # текущий цвет
        self.active_color = BLACK

        # размер кисти
        self.brush_size = 5

        # флаг рисования
        self.drawing = False

        # точки для фигур
        self.start_pos = None
        self.last_pos = None

        # текст режим
        self.text_active = False
        self.text_input = ""
        self.text_pos = None


    # сохранить рисунок
    def save_canvas(self):

        name = f"drawing_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pygame.image.save(self.canvas, name)


    # рисование фигур
    def draw_shape(self, surface, tool, p1, p2, color, size, offset_x=0):

        x1, y1 = p1[0] + offset_x, p1[1]
        x2, y2 = p2[0] + offset_x, p2[1]

        if tool == TOOL_LINE:
            pygame.draw.line(surface, color, (x1, y1), (x2, y2), size)

        elif tool == TOOL_RECT:
            pygame.draw.rect(surface, color,
                             (min(x1, x2), min(y1, y2),
                              abs(x2 - x1), abs(y2 - y1)), size)

        elif tool == TOOL_CIRCLE:
            pygame.draw.circle(surface, color,
                               ((x1 + x2) // 2, (y1 + y2) // 2),
                               int(math.hypot(x2 - x1, y2 - y1) / 2), size)


    # интерфейс слева (панель)
    def draw_ui(self):

        pygame.draw.rect(self.screen, BG_TOOLBAR, (0, 0, TOOLBAR_W, SCREEN_H))

        tools = [
            TOOL_PENCIL, TOOL_LINE, TOOL_RECT, TOOL_SQUARE,
            TOOL_CIRCLE, TOOL_RTRIANGLE, TOOL_EQTRIANGLE,
            TOOL_RHOMBUS, TOOL_FILL, TOOL_TEXT, TOOL_ERASER
        ]

        # кнопки инструментов
        for i, t in enumerate(tools):

            rect = pygame.Rect(10, 10 + i * 33, 160, 28)

            color = HIGHLIGHT if self.active_tool == t else (60, 60, 60)

            pygame.draw.rect(self.screen, color, rect, border_radius=4)

            label = self.font.render(t, True, WHITE)

            self.screen.blit(label, (20, 15 + i * 33))

        # палитра цветов
        for i, col in enumerate(PALETTE):

            r, c = divmod(i, 4)
            rect = pygame.Rect(10 + c * 42, 405 + r * 42, 35, 35)

            pygame.draw.rect(self.screen, col, rect)


    # обработка событий
    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # клавиатура
            if event.type == pygame.KEYDOWN:

                if self.text_active:

                    if event.key == pygame.K_RETURN:
                        txt = self.text_font.render(self.text_input, True, self.active_color)
                        self.canvas.blit(txt, self.text_pos)
                        self.text_active = False

                    elif event.key == pygame.K_BACKSPACE:
                        self.text_input = self.text_input[:-1]

                    else:
                        self.text_input += event.unicode


            # мышка нажата
            if event.type == pygame.MOUSEBUTTONDOWN:

                mx, my = event.pos

                # если клик по панели
                if mx < TOOLBAR_W:
                    self.active_tool = TOOL_PENCIL

                else:
                    # клик по холсту
                    self.drawing = True
                    self.start_pos = (mx - TOOLBAR_W, my)


            # мышь отпущена
            if event.type == pygame.MOUSEBUTTONUP:

                self.drawing = False


    # главный цикл
    def run(self):

        while True:

            self.handle_events()

            self.screen.fill(BLACK)

            # показываем холст
            self.screen.blit(self.canvas, (CANVAS_X, 0))

            # интерфейс
            self.draw_ui()

            pygame.display.flip()

            self.clock.tick(60)


# запуск программы
if __name__ == "__main__":
    PaintApp().run()