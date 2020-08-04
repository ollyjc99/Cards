import pygame
import random
from PIL import Image
from collections import namedtuple


def setup(win):
    width, height = win.get_size()

    card_width = round(width*.07)
    card_height = round(height*.15)

    x_spacing = width-(card_width*13)
    x_bord = round((x_spacing*.33) / 2)
    x_btwn = round((x_spacing*.66) / 13)

    y_spacing = height-(card_height*4)
    y_bord = round((y_spacing*.90) / 2)
    y_btwn = round((y_spacing*.10) / 2)

    # return card_width, card_height, x_bord, y_bord, x_btwn, y_btwn
    return card_width, card_height, [[[x, y] for x in range(x_bord, width-x_bord, card_width+x_btwn)] for y in range(round(y_bord*1.75), height-round(y_bord*.25), card_height+y_btwn)]

def print_title():
    oass


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


def pairs(win_width, win_height, base, deck):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('Pairs')
    win.fill((75,125,75))

    font = pygame.font.Font('static/font/Arial.ttf', 32)
    count = 0
    title = font.render('Pairs', True, (255,255,255))
    score = font.render('Score', True, (255,255,255))
    count = font.render(str(count), True, (255, 255, 255))

    title_rect = title.get_rect()
    title_rect.center = (round(win_width // 2), round(win_height * .20))

    score_rect = score.get_rect()
    score_rect.center = (round(win_width * .90), round(win_height * .05))

    count_rect = count.get_rect()
    count_rect.center = (round(win_width * .95), round(win_height * .05))

    win.blit(title, title_rect)
    win.blit(score, score_rect)
    win.blit(count, count_rect)

    card_width, card_height, grid = setup(win)
    deck = [base(win, card_width, card_height, suit, face) for face, suit in random.sample(deck, 52)]
    p_deck = iter(deck)

    first, second = None, None

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
