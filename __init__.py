import pygame
from Game import CGame
from MainMenu import CMainMenu
from GameOverMenu import CGameOverMenu
from Player import CPlayer
from Block import CBlock

# Initialization
pygame.init()
pygame.time.Clock().tick(60)

# Needed variables
Color_White = (255, 255, 255)
Color_Black = (0, 0, 0)
Color_Cyan = (0, 230, 255)
Color_Gray = (104, 104, 104)

# Game variables
WIDTH = 900
HEIGHT = 600
BLOCK_WIDTH = 10
BLOCK_HEIGHT = 10
UPDATE_TIME = 10
PLAYER_SPEED = 2

# Pygame objects
Window = pygame.display.set_mode((WIDTH, HEIGHT))

# Game screens
Game = CGame()
MainMenu = CMainMenu()
GameOverMenu = CGameOverMenu()

# Game objects
Player = CPlayer()
Block = CBlock()

# Main code
pygame.display.set_caption("Snake Game")
MainMenu.Activate()
while True:
    MainMenu.OnUpdate()
    Game.OnUpdate()
    GameOverMenu.OnUpdate()
