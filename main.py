import sys
import pygame

import constants

from gameloop import Game
from GameStates.menu import menu
from GameStates.levels import levels
from GameStates.customization import customization
from GameStates.shipgame import shipgame
from GameStates.gameover import gameover
from GameStates.victory import victory

# initialize pygame
pygame.init()

# create game window
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("The Aurora Armada")

states = {
    "menu": menu(),
    "levels": levels(),
    "customization": customization(),
    "shipgame": shipgame(),
    "gameover": gameover(),
    "victory": victory()
}

gameplay = Game(screen, states, "menu")
gameplay.run()

pygame.quit()
sys.exit()