import pygame
import random
from PIL import Image
from collections import namedtuple


def pairs(win, deck):
    print(win.get_size())
    grid = [[[x, y] for x in range(66, 734, 100+13)] for y in range(71, 529, 128+35)]
    deck = iter([random.choice(deck) for i in range(0, 18)])

    for row in grid:
        for col in row:
            card = next(deck)
            card.draw(col)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
