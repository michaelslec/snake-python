import pygame


class Game():
    FPS = 15
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    CELLSIZE = 20
    assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOW_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
    CELLWIDTH = int(WINDOW_WIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOW_HEIGHT / CELLSIZE)

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0,   0,   0)
    RED = (255,   0,   0)
    GREEN = (0, 255,   0)
    DARKGREEN = (0, 155,   0)
    DARKGRAY = (40,  40,  40)
    BG_COLOR = BLACK

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Wormy')

    def showStartScreen(self):
        titleFont = pygame.font.Font('freesansbold.ttf', 100)
        titleSurf1 = titleFont.render(
            'Wormy!', True, self.WHITE, self.DARKGREEN)
        titleSurf2 = titleFont.render('Wormy!', True, self.GREEN)
        degrees1 = 0
        degrees2 = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.run()
            self.screen.fill(self.BG_COLOR)
            rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
            rotatedRect1 = rotatedSurf1.get_rect()
            rotatedRect1.center = (self.WINDOW_WIDTH / 2,
                                   self.WINDOW_HEIGHT / 2)
            self.screen.blit(rotatedSurf1, rotatedRect1)

            rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
            rotatedRect2 = rotatedSurf2.get_rect()
            rotatedRect2.center = (self.WINDOW_WIDTH / 2,
                                   self.WINDOW_HEIGHT / 2)
            self.screen.blit(rotatedSurf2, rotatedRect2)

            self.drawPressKeyMsg()

            pygame.display.update()
            self.clock.tick(self.FPS)
            degrees1 += 3  # rotate by 3 degrees each frame
            degrees2 += 7  # rotate by 7 degrees each frame

    def drawPressKeyMsg(self):
        pressKeySurf = self.BASICFONT.render(
            'Press a key to play.', True, self.DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (self.WINDOW_WIDTH - 200,
                                self.WINDOW_HEIGHT - 30)
        self.screen.blit(pressKeySurf, pressKeyRect)

    def handleKeyEvents(self, event):
        print(event)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)

            self.screen.fill(self.BG_COLOR)
            pygame.display.flip()
