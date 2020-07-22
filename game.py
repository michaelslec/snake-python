import pygame


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.fill((255, 255, 255))
            pygame.display.flip()
