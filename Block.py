import __init__
import pygame
from random import randint

class CBlock:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Color = [255, 255, 255]
        self.Rect = pygame.Rect(self.X, self.Y, __init__.BLOCK_WIDTH, __init__.BLOCK_HEIGHT)

        self.GeneratePosition()

    def GeneratePosition(self):
        self.X = randint(1, (__init__.WIDTH - (1 + __init__.BLOCK_WIDTH)))
        self.Y = randint(1, (__init__.HEIGHT - (1 + __init__.BLOCK_HEIGHT)))

        self.Color[0] = randint(0, 255)
        self.Color[1] = randint(0, 255)
        self.Color[2] = randint(0, 255)

        self.Rect.x = self.X
        self.Rect.y = self.Y

    def Draw(self):
        pygame.draw.rect(__init__.Window, self.Color, self.Rect)

    def Update(self):
        if not __init__.Player.Rect.colliderect(self.Rect):
            return

        self.GeneratePosition()
        __init__.Player.AddBlock(self.Color)
