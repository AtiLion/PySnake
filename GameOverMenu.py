import __init__
import pygame
import math
import sys

class CGameOverMenu:
    def __init__(self):
        self.Font_GameOver = pygame.font.SysFont("impact", 72)
        self.Font_Score = pygame.font.SysFont("arial", 40)
        self.Font_Button = pygame.font.SysFont("arial", 100)

        self.Color_Restart = __init__.Color_White
        self.Color_Exit = __init__.Color_White

        self.Text_GameOver = self.Font_GameOver.render("Game Over", True, __init__.Color_Cyan)
        self.Text_Restart = self.Font_Button.render("Restart", True, __init__.Color_Black)
        self.Text_Exit = self.Font_Button.render("Exit", True, __init__.Color_Black)

        self.Button_Restart = pygame.Rect((math.ceil(__init__.WIDTH / 2) - (math.ceil(self.Font_Button.size("Restart")[0] / 2) + 50)),
                                          300,
                                          (math.ceil(self.Font_Button.size("Restart")[0]) + 100),
                                          100)
        self.Button_Exit = pygame.Rect((math.ceil(__init__.WIDTH / 2) - (math.ceil(self.Font_Button.size("Exit")[0] / 2) + 50)),
                                       450,
                                       (math.ceil(self.Font_Button.size("Exit")[0]) + 100),
                                       100)

        self.Active = False

    def Activate(self):
        __init__.Game.Deactivate()

        self.Active = True

    def Deactivate(self):
        self.Active = False

    def Update_Button(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        mouse_pos = pygame.mouse.get_pos()
        if self.Button_Restart.collidepoint(mouse_pos):
            self.Deactivate()
            __init__.Game.Activate()
        elif self.Button_Exit.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()

    def OnUpdate(self):
        if not self.Active:
            return

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.Update_Button(event)
        if self.Button_Restart.collidepoint(mouse_pos):
            self.Color_Restart = __init__.Color_Gray
        else:
            self.Color_Restart = __init__.Color_White
        if self.Button_Exit.collidepoint(mouse_pos):
            self.Color_Exit = __init__.Color_Gray
        else:
            self.Color_Exit = __init__.Color_White

        self.OnDraw()
        pygame.display.update()

    def OnDraw(self):
        Text_Score = self.Font_Score.render("Score: " + str(len(__init__.Player.Blocks)), True, __init__.Color_Cyan)

        __init__.Window.fill(__init__.Color_Black)

        __init__.Window.blit(self.Text_GameOver,
                             ((math.ceil(__init__.WIDTH / 2) - (math.ceil(self.Font_GameOver.size("Game Over")[0] / 2))),
                              50))
        __init__.Window.blit(Text_Score,
                             ((math.ceil(__init__.WIDTH / 2) - (math.ceil(self.Font_Score.size("Score: " + str(len(__init__.Player.Blocks)))[0] / 2))),
                              150))

        pygame.draw.rect(__init__.Window, self.Color_Restart, self.Button_Restart)
        __init__.Window.blit(self.Text_Restart, ((self.Button_Restart.x + 50), self.Button_Restart.y - 10))
        pygame.draw.rect(__init__.Window, self.Color_Exit, self.Button_Exit)
        __init__.Window.blit(self.Text_Exit, ((self.Button_Exit.x + 50), self.Button_Exit.y - 10))