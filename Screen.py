import time
import sys
import pygame
import random

pygame.init()

size = display_width, display_height = 1200, 600
center = (display_width / 2, display_height / 2)

black = 25, 25, 25
purple = (23, 5, 54)
fps = 30

game_display = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.image.load('Sprite.png')
