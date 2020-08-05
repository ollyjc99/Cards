import pygame
import random


def setup(win, bus_len):
    width, height = win.get_size()

    card_width = round(width*.098)
    card_height = round(height*.167)
    # grid = [[x,y] for x in range(

    return card_width, card_height, 'grid'


def bus(win_width, win_height, base, deck, bus_len, clock):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('The Bus')
    background_colour = (75, 125, 75)
    win.fill(background_colour)

    card_width, card_height, grid = setup(win, bus_len)
    deck = [base(win, card_width, card_height, suit, face) for face, suit in random.sample(deck, 52)]
    p_deck = iter(deck)

    running = True
    while running:
        clock(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

