import pygame
import random
from misc import *


def setup(win, deck):
    width, height = win.get_size()

    card_width = round(width*.07)
    card_height = round(height*.15)

    x_spacing = width-(card_width*13)
    x_bord = round((x_spacing*.33) / 2)
    x_btwn = round((x_spacing*.66) / 13)

    y_spacing = height-(card_height*4)
    y_bord = round((y_spacing*.90) / 2)
    y_btwn = round((y_spacing*.10) / 2)

    return [[[x, y] for x in range(x_bord, width-x_bord, card_width+x_btwn)] for y in range(round(y_bord*1.75), height-round(y_bord*.25), card_height+y_btwn)]


def print_score(win, win_width, win_height, font, count):

    pair_count = font.render(str(count), True, (255, 255, 255), (75,125,75))

    count_rect = pair_count.get_rect()
    count_rect.center = (round(win_width * .96), round(win_height * .05))

    win.blit(pair_count, count_rect)


def pairs(win_width, win_height, deck, clock):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('Pairs')
    background_colour = (75,125,75)
    win.fill(background_colour)

    font = pygame.font.Font('static/font/Arial.ttf', 32)
    count = 0
    title = font.render('Pairs', True, (255,255,255))
    score = font.render('Score', True, (255,255,255))

    title_rect = title.get_rect()
    title_rect.center = (round(win_width // 2), round(win_height * .20))

    score_rect = score.get_rect()
    score_rect.center = (round(win_width * .90), round(win_height * .05))

    win.blit(title, title_rect)
    win.blit(score, score_rect)

    print_score(win, win_width, win_height, font, count)
    grid = setup(win, deck)

    p_deck = iter(deck.cards)
    cards = pygame.sprite.Group()
    cards.add(deck.cards)

    first, second = None, None
    for row in grid:
        for col in row:
            card = next(p_deck)
            card.rect.x, card.rect.y = col

    cards.add(deck.cards)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for card in deck.cards:
                    if card.rect.collidepoint(event.pos):
                        if not card.flipped:
                            if not first:
                                first = card
                                flip(card)
                            elif first and not second:
                                flip(card)
                                second = card
                                if first.face == second.face:
                                    count += 1
                                    print_score(win, win_width, win_height, font, count)
                                    first, second = None, None
                                else:
                                    pygame.time.wait(1000)
                                    flip(first)
                                    flip(second)
                                    first, second = None, None
                            else:
                                pass

        cards.update()
        cards.draw(win)
        pygame.display.update()
        clock.tick(60)
