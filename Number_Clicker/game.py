import pygame
from number_object import NumberObject
from utils import generate_numbers

# ゲームのクラス
class Game:
    def __init__(self):
        pygame.init()

        # ウィンドウのサイズ
        self.WIDTH = 800
        self.HEIGHT = 600

        # ゲームウィンドウの作成
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Number Clicker")

        self.clock = pygame.time.Clock()

        self.number_objects = []
        generate_numbers(self.number_objects)

        self.start_time = pygame.time.get_ticks()
        self.current_number = 1
        self.game_over = False

    def run(self):
        running = True

        while running:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over and self.current_number <= 20:
                        for obj in self.number_objects:
                            obj.is_clicked(pygame.mouse.get_pos())
                            if obj.clicked and obj.number == self.current_number:
                                self.number_objects.remove(obj)
                                self.current_number += 1
                                break

            for obj in self.number_objects:
                obj.draw(self.screen)

            if self.current_number > 20 and not self.game_over:
                self.game_over = True
                elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000

            if self.game_over:
                font = pygame.font.Font(None, 72)
                text = font.render("Game Over", True, (255, 0, 0))
                text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
                self.screen.blit(text, text_rect)
                time_text = font.render("Time: {:.2f} seconds".format(elapsed_time), True, (255, 0, 0))
                time_rect = time_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))
                self.screen.blit(time_text, time_rect)
            else:
                elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
                font = pygame.font.Font(None, 36)
                time_text = font.render("Time: {:.2f} seconds".format(elapsed_time), True, (0, 0, 0))
                time_rect = time_text.get_rect(topright=(self.WIDTH - 20, 20))
                self.screen.blit(time_text, time_rect)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
