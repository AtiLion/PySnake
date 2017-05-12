import __init__
import pygame
import sys
import math

class CMainMenu:
    def __init__(self):
        self.Font_Title = pygame.font.SysFont("impact", 72)
        self.Font_Button = pygame.font.SysFont("arial", 100)

        self.Color_Start = __init__.Color_White
        self.Color_Exit = __init__.Color_White

        self.Text_Title = self.Font_Title.render("Snake Game", True, __init__.Color_Cyan)
        self.Text_Start = self.Font_Button.render("Start Game", True, __init__.Color_Black)
        self.Text_Exit = self.Font_Button.render("Exit", True, __init__.Color_Black)

        self.Button_Start = pygame.Rect((math.ceil(__init__.WIDTH / 2) - (math.ceil(self.Font_Button.size("Start Game")[0] / 2) + 50)),
                                        250,
                                        (math.ceil(self.Font_Button.size("Start Game")[0]) + 100),
                                        100)
        self.Button_Exit = pygame.Rect((math.ceil(__init__.WIDTH / 2) - (math.ceil(self.Font_Button.size("Exit")[0] / 2) + 50)),
                                       400,
                                       (math.ceil(self.Font_Button.size("Exit")[0]) + 100),
                                       100)

        self.Active = False

    def Activate(self):
        self.Active = True

    def Deactivate(self):
        self.Active = False

    def Update_Button(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        mouse_pos = pygame.mouse.get_pos()
        if self.Button_Start.collidepoint(mouse_pos):
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
        if self.Button_Start.collidepoint(mouse_pos):
            self.Color_Start = __init__.Color_Gray
        else:
            self.Color_Start = __init__.Color_White
        if self.Button_Exit.collidepoint(mouse_pos):
            self.Color_Exit = __init__.Color_Gray
        else:
            self.Color_Exit = __init__.Color_White

        self.OnDraw()
        pygame.display.update()

    def OnDraw(self):
        __init__.Window.fill(__init__.Color_Black)

        __init__.Window.blit(self.Text_Title,
                             ((math.ceil(__init__.WIDTH / 2) - (math.ceil(self.Font_Title.size("Snake Game")[0] / 2))),
                              100))

        pygame.draw.rect(__init__.Window, self.Color_Start, self.Button_Start)
        __init__.Window.blit(self.Text_Start, ((self.Button_Start.x + 50), self.Button_Start.y - 10))
        pygame.draw.rect(__init__.Window, self.Color_Exit, self.Button_Exit)
        __init__.Window.blit(self.Text_Exit, ((self.Button_Exit.x + 50), self.Button_Exit.y - 10))
