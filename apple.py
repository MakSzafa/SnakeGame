import pygame

class Apple:

    x = 0
    y = 0
    step = 50

    def __init__(self, x, y):

        self.x = x * self.step
        self.y = y * self.step

    def draw(self,screen):

        rect = pygame.Rect(self.x, self.y, 50, 50)
        pygame.draw.rect(screen, (0, 128, 0), rect)