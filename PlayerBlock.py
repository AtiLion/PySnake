import __init__
import pygame

class CPlayerBlock:
    def __init__(self, direction, color):
        x = __init__.Player.Rect.x
        y = __init__.Player.Rect.y

        if len(__init__.Player.Blocks) > 0:
            x = __init__.Player.Blocks[len(__init__.Player.Blocks) - 1].Rect.x
            y = __init__.Player.Blocks[len(__init__.Player.Blocks) - 1].Rect.y

        if direction == 1:
            y = y + __init__.BLOCK_HEIGHT
        elif direction == 2:
            y = y - __init__.BLOCK_HEIGHT
        elif direction == 3:
            x = x + __init__.BLOCK_WIDTH
        elif direction == 4:
            x = x - __init__.BLOCK_WIDTH

        self.Direction = direction
        self.Color = color
        self.Switch = []
        self.PreviousTicks = pygame.time.get_ticks()
        self.Rect = pygame.Rect(x, y, __init__.BLOCK_WIDTH, __init__.BLOCK_HEIGHT)

    def Update(self):
        if not __init__.Player.Alive:
            return

        if len(self.Switch) > 0:
            if self.Switch[0][1] == self.Rect.x and self.Switch[0][2] == self.Rect.y:
                self.Direction = self.Switch[0][0]
                self.Switch.remove(self.Switch[0])

        tmpTicks = pygame.time.get_ticks()
        if (tmpTicks - self.PreviousTicks) >= __init__.UPDATE_TIME:
            if self.Direction == 1:
                self.Rect.y = self.Rect.y - __init__.PLAYER_SPEED
            elif self.Direction == 2:
                self.Rect.y = self.Rect.y + __init__.PLAYER_SPEED
            elif self.Direction == 3:
                self.Rect.x = self.Rect.x - __init__.PLAYER_SPEED
            elif self.Direction == 4:
                self.Rect.x = self.Rect.x + __init__.PLAYER_SPEED
            self.PreviousTicks = tmpTicks

        if __init__.Player.Rect.colliderect(self.Rect) and __init__.Player.Blocks[0].Rect != self.Rect:
            __init__.Player.Alive = False
            __init__.GameOverMenu.Activate()

    def Draw(self):
        pygame.draw.rect(__init__.Window, self.Color, self.Rect)
