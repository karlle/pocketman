import pygame
from game_model import Model

class Controller():

    def __init__(self, screenWidth, screenHeight, hitboxes = False):
        self.model = Model(screenWidth, screenHeight, hitboxes)
        self.gameLoop()

    """
    The actual game loop, loops at 27 fps and registers key presses until
    the x in the upper right corner is pressed
    """

    def gameLoop(self):

        clock = pygame.time.Clock()
        run = True

        while run:

            clock.tick(27)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.model.paus()

            if keys[pygame.K_RETURN]:
                self.model.enter()

            if keys[pygame.K_LEFT]:
                self.model.walkLeft()

            if keys[pygame.K_RIGHT]:
                self.model.walkRight()

            if keys[pygame.K_UP]:
                self.model.jump()

            if keys[pygame.K_SPACE]:
                self.model.fire()

            if keys[pygame.K_BACKSPACE]:
                self.model.removeCharFromName()

            # for chars a-z
            for (i, k) in enumerate(keys[97:123]):
                if k:
                    self.model.addCharToName(i)

            # update the model at every frame, even if no keypresses occur
            self.model.update()


screenWidth = 800
screenHeight = 480
c = Controller(screenWidth, screenHeight, hitboxes = False)
