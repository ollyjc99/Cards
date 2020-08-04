import pygame
import random
from PIL import Image
from collections import namedtuple


def flip(card):
    card.flipped = not card.flipped
    card.im = card.flip()
    card.draw((card.x, card.y))
    pygame.display.update()


def match(first, second):
    if first.face == second.face:
        return True
    else:
        return False


def pairs(win, deck):
    print(win.get_size())
    grid = [[[x, y] for x in range(13, 1267, 90+7)] for y in range(187, 960-187, 115+36)]
    deck = random.sample(deck, 52)
    p_deck = iter(deck)
    win.fill((75,125,75))
    pygame.display.set_caption('Pairs')
    count = 0
    first, second = None, None

    for row in grid:
        for col in row:
            card = next(p_deck)
            count +=1

            print(count)
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
                        if not card.flipped:
                            if not first:
                                first = card
                                flip(card)
                            elif first and not second:
                                flip(card)
                                second = card
                                if match(first, second):
                                    first, second = None, None
                                else:
                                    pygame.time.wait(1000)
                                    flip(first)
                                    flip(second)
                                    first, second = None, None
                            else:
                                pass

        pygame.display.update()
