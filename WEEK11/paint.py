import pygame
import math

# ================= INITIALIZATION =================
def main():
    pygame.init()

    # создаём окно программы
    screen = pygame.display.set_mode((640, 520))
    pygame.display.set_caption("Paint Project")

    clock = pygame.time.Clock()
    radius = 15
    mode = 'draw'
    points = []
    start_pos = None

    # список всех нарисованных объектов
    drawings = []

    # текущий выбранный цвет
    current_color = (0, 0, 255)

    # палитра цветов
    colors = [
        (255,0,0), (0,255,0), (0,0,255),
        (255,255,0), (0,255,255), (255,165,0)
    ]

    WHITE = (255, 255, 255)

    # ================= BUTTONS =================
    # кнопки режимов рисования
    buttons = [
        ("Draw", 'draw', 10),
        ("Rect", 'rect', 80),
        ("Square", 'square', 150),
        ("RTri", 'right_tri', 230),
        ("ETri", 'eq_tri', 310),
        ("Rhomb", 'rhombus', 390),
        ("Circle", 'circle', 470),
        ("Eraser", 'eraser', 550),
    ]

    running = True

    #  MAIN LOOP 
    while running:

        mouse_pos = pygame.mouse.get_pos()

        #  EVENTS 
        for event in pygame.event.get():

            # закрытие окна
            if event.type == pygame.QUIT:
                running = False

            # MOUSE CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # выбор режима (кнопки)
                    for (label, btn_mode, bx) in buttons:
                        btn_rect = pygame.Rect(bx, 450, 60, 25)
                        if btn_rect.collidepoint(event.pos):
                            mode = btn_mode

                    # выбор цвета
                    for i, color in enumerate(colors):
                        color_rect = pygame.Rect(10 + i * 35, 480, 25, 25)
                        if color_rect.collidepoint(event.pos):
                            current_color = color

                    # сохраняем начальную точку
                    start_pos = event.pos
                    points = []

            #  DRAWING (MOUSE MOVE)
            if event.type == pygame.MOUSEMOTION:

                # рисование свободной линией
                if mode == 'draw':
                    points.append(event.pos)

                    # сохраняем линию как сегменты
                    if len(points) >= 2:
                        drawings.append(('line', current_color,
                                         points[-2], points[-1], radius))

                # ластик
                elif mode == 'eraser':
                    drawings.append(('eraser', (0,0,0),
                                     event.pos, radius * 2))

            # MOUSE RELEASE
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:

                    x1, y1 = start_pos
                    x2, y2 = event.pos

                    # RECTANGLE 
                    if mode == 'rect':
                        x = min(x1, x2)
                        y = min(y1, y2)
                        w = abs(x2 - x1)
                        h = abs(y2 - y1)

                        drawings.append(('rect', current_color, (x, y, w, h)))

                    #  SQUARE 
                    elif mode == 'square':
                        size = max(abs(x2 - x1), abs(y2 - y1))
                        drawings.append(('rect', current_color,
                                         (x1, y1, size, size)))

                    # RIGHT TRIANGLE
                    elif mode == 'right_tri':
                        points_tri = [
                            (x1, y1),
                            (x1, y2),
                            (x2, y2)
                        ]
                        drawings.append(('poly', current_color, points_tri))

                    #  EQUILATERAL TRIANGLE 
                    elif mode == 'eq_tri':
                        side = abs(x2 - x1)
                        height = int((math.sqrt(3)/2) * side)

                        points_tri = [
                            (x1, y1),
                            (x1 + side, y1),
                            (x1 + side//2, y1 - height)
                        ]
                        drawings.append(('poly', current_color, points_tri))

                    # RHOMBUS
                    elif mode == 'rhombus':
                        cx = (x1 + x2) // 2
                        cy = (y1 + y2) // 2
                        dx = abs(x2 - x1) // 2
                        dy = abs(y2 - y1) // 2

                        points_r = [
                            (cx, y1),
                            (x2, cy),
                            (cx, y2),
                            (x1, cy)
                        ]
                        drawings.append(('poly', current_color, points_r))

                    #  CIRCLE 
                    elif mode == 'circle':
                        dx = x2 - x1
                        dy = y2 - y1
                        r = int((dx**2 + dy**2) ** 0.5)

                        drawings.append(('circle', current_color,
                                         start_pos, r))

                    start_pos = None
                    points = []

        #  BACKGROUND 
        # очищаем экран каждый кадр
        screen.fill((0, 0, 0))

        # DRAW SAVED OBJECTS
        for d in drawings:

            # линия
            if d[0] == 'line':
                drawLine(screen, d[2], d[3], d[4], d[1])

            # прямоугольник
            elif d[0] == 'rect':
                pygame.draw.rect(screen, d[1], d[2], 2)

            # круг
            elif d[0] == 'circle':
                pygame.draw.circle(screen, d[1], d[2], d[3], 2)

            # ластик
            elif d[0] == 'eraser':
                pygame.draw.circle(screen, d[1], d[2], d[3])

            # многоугольники (треугольники, ромб)
            elif d[0] == 'poly':
                pygame.draw.polygon(screen, d[1], d[2], 2)

        #  UI PANEL 
        pygame.draw.rect(screen, (50, 50, 50), (0, 440, 640, 80))

        # кнопки режимов
        for (label, btn_mode, bx) in buttons:
            color = (180, 180, 180) if mode == btn_mode else (120, 120, 120)
            pygame.draw.rect(screen, color, (bx, 450, 60, 25))

            txt = pygame.font.SysFont("Verdana", 9).render(label, True, (0,0,0))
            screen.blit(txt, (bx + 3, 455))

        # палитра цветов
        for i, color in enumerate(colors):
            pygame.draw.rect(screen, color, (10 + i * 35, 480, 25, 25))

            if color == current_color:
                pygame.draw.rect(screen, WHITE,
                                 (10 + i * 35, 480, 25, 25), 2)

        pygame.display.flip()
        clock.tick(60)

#  LINE DRAW FUNCTION
def drawLine(screen, start, end, width, color):

    dx = start[0] - end[0]
    dy = start[1] - end[1]

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return

    # рисуем плавную линию через точки
    for i in range(steps):
        t = i / steps
        x = int(start[0] * (1 - t) + end[0] * t)
        y = int(start[1] * (1 - t) + end[1] * t)

        pygame.draw.circle(screen, color, (x, y), width)

# запускаем программу
main()