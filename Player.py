import __init__
import pygame
import math
from PlayerBlock import CPlayerBlock

class CPlayer:
    def __init__(self):
        self.PreviousTicks = pygame.time.get_ticks()
        self.Blocks = []
        self.Alive = False
        self.Direction = 0  # 0 = None, 1 = Up, 2 = Down, 3 = Left, 4 = Right
        self.Rect = pygame.Rect(math.ceil((__init__.WIDTH / 2) - math.ceil(__init__.BLOCK_WIDTH / 2)),
                                math.ceil((__init__.HEIGHT / 2) - math.ceil(__init__.BLOCK_HEIGHT / 2)),
                                __init__.BLOCK_WIDTH,
                                __init__.BLOCK_HEIGHT)

    def ChangeDirection(self, direction):
        self.Direction = direction
        for i, v in enumerate(self.Blocks):
            v.Switch.append((direction,
                             self.Rect.x,
                             self.Rect.y))

    def SpawnPlayer(self):
        self.Rect.x = math.ceil((__init__.WIDTH / 2) - 1)
        self.Rect.y = math.ceil((__init__.HEIGHT / 2) - 1)
        self.Blocks = []
        self.Direction = 0
        self.Alive = True

    def AddBlock(self):
        direction = self.Direction

        if len(self.Blocks) > 0:
            direction = self.Blocks[len(self.Blocks) - 1].Direction

        playerblock = CPlayerBlock(direction)

        if len(self.Blocks) > 0:
            for i, v in enumerate(self.Blocks[len(self.Blocks) - 1].Switch):
                playerblock.Switch.append(v)

        self.Blocks.append(playerblock)

    def DrawPlayer(self):
        if not self.Alive:
            return

        pygame.draw.rect(__init__.Window, __init__.Color_White, self.Rect)

        for i, v in enumerate(self.Blocks):
            v.Draw()

    def Update(self):
        if not self.Alive:
            return

        tmpTicks = pygame.time.get_ticks()
        if(tmpTicks - self.PreviousTicks) >= __init__.UPDATE_TIME:
            if self.Direction == 1:
                self.Rect.y = self.Rect.y - __init__.PLAYER_SPEED
            elif self.Direction == 2:
                self.Rect.y = self.Rect.y + __init__.PLAYER_SPEED
            elif self.Direction == 3:
                self.Rect.x = self.Rect.x - __init__.PLAYER_SPEED
            elif self.Direction == 4:
                self.Rect.x = self.Rect.x + __init__.PLAYER_SPEED
            self.PreviousTicks = tmpTicks

        for i, v in enumerate(self.Blocks):
            v.Update()

        if (self.Rect.x > __init__.WIDTH or self.Rect.x < 0) or (self.Rect.y > __init__.HEIGHT or self.Rect.y < 0):
            self.Alive = False
            __init__.GameOverMenu.Activate()
