import pygame
import random
from PIL import Image
from collections import namedtuple


def pattern_gen(win, deck):
    pos = win.get_size()
    x = int(pos[0]/2-50)
    y = int(pos[1]/2-69)
    card = random.choice(deck)
    card.draw((x,y))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
