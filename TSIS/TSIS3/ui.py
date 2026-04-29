import pygame


# кнопка (для меню и интерфейса)
class Button:
    def __init__(self, x, y, w, h, text, color=(200, 200, 200), hover_color=(150, 150, 150)):

        # прямоугольник кнопки
        self.rect = pygame.Rect(x, y, w, h)

        # текст кнопки
        self.text = text

        # обычный цвет
        self.color = color

        # цвет при наведении мышки
        self.hover_color = hover_color

        # шрифт
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):

        # позиция мыши
        mouse_pos = pygame.mouse.get_pos()

        # если мышь на кнопке — другой цвет
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        # рисуем кнопку
        pygame.draw.rect(surface, current_color, self.rect)

        # рамка
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

        # текст кнопки
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)

        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):

        # проверка клика мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if self.rect.collidepoint(event.pos):
                return True

        return False


# поле ввода текста (например имя игрока)
class TextInput:
    def __init__(self, x, y, w, h):

        # область ввода
        self.rect = pygame.Rect(x, y, w, h)

        # текст который вводим
        self.text = ""

        # шрифт
        self.font = pygame.font.Font(None, 36)

    def handle_event(self, event):

        # обработка клавиатуры
        if event.type == pygame.KEYDOWN:

            # удалить символ
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]

            # добавить символ
            elif event.unicode.isprintable() and len(self.text) < 15:
                self.text += event.unicode

    def draw(self, surface):

        # фон поля
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

        # рамка
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

        # текст внутри поля
        text_surf = self.font.render(self.text, True, (0, 0, 0))

        surface.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))