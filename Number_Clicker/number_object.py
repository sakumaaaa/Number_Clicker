import pygame

# 数字のオブジェクトを表すクラス
class NumberObject:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.clicked = False

    def draw(self, screen):
        if not self.clicked:
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 20)
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.number), True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.x, self.y))
            screen.blit(text, text_rect)

    def is_clicked(self, pos):
        distance = ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) ** 0.5
        if distance <= 20:
            self.clicked = True
