import pygame
import datetime


# КИСТЬ
def draw_pencil(screen, prev, pos, color, size):

    # рисуем линию между точками
    if prev:
        pygame.draw.line(screen, color, prev, pos, size)

    return pos


# ЛИНИЯ
def draw_line(screen, start, end, color, size):

    pygame.draw.line(screen, color, start, end, size)


def preview_line(screen, start, end, color, size):

    temp = screen.copy()

    pygame.draw.line(temp, color, start, end, size)

    screen.blit(temp, (0, 0))


# ЗАЛИВКА
def flood_fill(surface, pos, new_color):

    x, y = pos
    target = surface.get_at((x, y))

    if target == new_color:
        return

    stack = [(x, y)]

    while stack:

        x, y = stack.pop()

        if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():

            if surface.get_at((x, y)) == target:

                surface.set_at((x, y), new_color)

                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))


# СОХРАНЕНИЕ
def save_canvas(screen):

    filename = datetime.datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")

    pygame.image.save(screen, filename)

    print("Saved:", filename)


# ТЕКСТ
def handle_text(event, text, screen, pos, color, font):

    if event.key == pygame.K_RETURN:

        screen.blit(font.render(text, True, color), pos)

        return "", False

    elif event.key == pygame.K_ESCAPE:

        return "", False

    else:

        return text + event.unicode, True