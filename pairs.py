import pygame
import random
from PIL import Image
from collections import namedtuple


def pairs(win, deck):
    print(win.get_size())
    grid = [[[x, y] for x in range(66, 734, 100+13)] for y in range(71, 529, 128+35)]
    deck = random.sample(deck, 18)
    p_deck = iter(deck)
    win.fill((75,125,75))

    for row in grid:
        for col in row:
            card = next(p_deck)
            card.x, card.y = col
            card.draw(col)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for card in deck:
                    if card.im.get_rect(x=card.x, y=card.y).collidepoint(event.pos):
                        card.flipped = not card.flipped
                        card.im = card.flip()
                        card.draw((card.x, card.y))

        pygame.display.update()
