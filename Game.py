import __init__
import pygame
import sys

class CGame:
    def __init__(self):
        self.Active = False

    def Activate(self):
        __init__.GameOverMenu.Deactivate()
        __init__.MainMenu.Deactivate()

        __init__.Player.SpawnPlayer()

        self.Active = True

    def Deactivate(self):
        __init__.Player.Alive = False

        self.Active = False

    def Update_Keys(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            __init__.Player.ChangeDirection(1)
        elif event.key == pygame.K_DOWN:
            __init__.Player.ChangeDirection(2)
        elif event.key == pygame.K_LEFT:
            __init__.Player.ChangeDirection(3)
        elif event.key == pygame.K_RIGHT:
            __init__.Player.ChangeDirection(4)

    def OnUpdate(self):
        if not self.Active:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.Update_Keys(event)

        __init__.Player.Update()
        __init__.Block.Update()

        self.OnDraw()
        pygame.display.update()

    def OnDraw(self):
        __init__.Window.fill(__init__.Color_Black)

        __init__.Player.DrawPlayer()
        __init__.Block.Draw()
