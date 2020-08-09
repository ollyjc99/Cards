import pygame
import random
import time


def setup(win):
    w, h = win.get_size()

    card_width = round(w*.098)
    card_height = round(h*.167)

    return card_width, card_height


def card_check(card, pos):
    if card.im.get_rect(x=card.x, y=card.y).collidepoint(pos):
        return True
    else:
        return False



def flip(card):
    card.flipped = not card.flipped
    card.im = card.flip()
    card.draw((card.x, card.y))
    pygame.display.update()


def redraw_win(win, card):
    win.fill((75, 125, 75))
    card.move(pygame.mouse.get_pos())
    pygame.display.update()


def sandbox(win_width, win_height, base, deck, clock):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('The Bus')
    background_colour = (75, 125, 75)
    win.fill(background_colour)

    card_width, card_height = setup(win)
    deck = [base(win, card_width, card_height, suit, face) for face, suit in random.sample(deck, 52)]
    card = random.choice(deck)
    print(f'{card.face} of {card.suit}')
    card.draw((250,250))

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True
                    for card in deck:
                        if card_check(card, event.pos):
                            while pressed:
                                for e in pygame.event.get():
                                    if e.type != pygame.MOUSEBUTTONUP:
                                        redraw_win(win, card)
                                        card.set_rect()
                                    elif e.type == pygame.MOUSEBUTTONUP:
                                        pressed = False

                elif event.button == 3:
                    for card in deck:
                        if card_check(card, event.pos):
                            flip(card)

        pygame.display.update()

