import pygame
import random


def setup(win, bus_len):
    w, h = win.get_size()

    card_width = round(w*.098)
    card_height = round(h*.167)

    x_spacing = round(w-(card_width * bus_len))
    x_bord = 242
    x_btwn = 10

    y = round((h // 2) - card_height / 2)

    grid = [[x,y] for x in range(x_bord, w-x_bord, card_width+x_btwn)]

    return card_width, card_height, grid


def flip(card):
    card.flipped = not card.flipped
    card.im = card.flip()
    card.draw((card.x, card.y))
    pygame.display.update()


def bus(win_width, win_height, base, deck, bus_len, clock):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('The Bus')
    background_colour = (75, 125, 75)
    win.fill(background_colour)

    card_width, card_height, grid = setup(win, bus_len)
    deck = [base(win, card_width, card_height, suit, face) for face, suit in random.sample(deck, bus_len)]
    p_deck = iter(deck)

    for row in grid:
        print(row)
        card = next(p_deck)
        card.x, card.y = row
        card.draw(row)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for card in deck:
                    if card.im.get_rect(x=card.x, y=card.y).collidepoint(event.pos):
                        flip(card)
        pygame.display.update()

