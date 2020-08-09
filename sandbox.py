import pygame
import random
import time


def setup(win, deck):
    w, h = win.get_size()

    card_width = round(w*.098)
    card_height = round(h*.167)

    for card in deck.cards:
        card.x = deck.x
        card.y = deck.y
        card.width = card_width
        card.height = card_height


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


def redraw_win(win, card, deck, hand):
    win.fill((75, 125, 75))
    deck.draw()
    if hand:
        for card in hand:
            card.draw()
    card.move(pygame.mouse.get_pos())
    pygame.display.update()


def sandbox(win_width, win_height, deck, clock):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('The Bus')
    win.fill((75, 125, 75))

    deck.draw((win_width // 2,win_height // 2))
    setup(win, deck)
    hand = []
    card = random.choice(deck.cards)

    print(f'{card.face} of {card.suit}')

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                if event.button == 1:
                    if hand:
                        for card in hand:
                            if card_check(card, event.pos):
                                while pressed:
                                    for e in pygame.event.get():
                                        if e.type != pygame.MOUSEBUTTONUP:
                                            redraw_win(win, card, deck, hand)
                                            card.set_rect()
                                        elif e.type == pygame.MOUSEBUTTONUP:
                                            pressed = False

                    if deck.cards:
                        if card_check(deck.cards[0], event.pos):
                            card = deck.cards[0]
                            hand.append(card)
                            print(deck.cards[0].face)
                            deck.cards.pop(0)
                            for card in hand:
                                print(f'{card.face} of {card.suit}')
                            while pressed:
                                for e in pygame.event.get():
                                    if e.type != pygame.MOUSEBUTTONUP:
                                        redraw_win(win, card, deck, hand)
                                        card.set_rect()
                                    elif e.type == pygame.MOUSEBUTTONUP:
                                        pressed = False

                elif event.button == 2:
                    for card in deck.cards:
                        print(f'{card.face} of {card.suit}')

                elif event.button == 3:
                    if hand:
                        for card in hand:
                            if card_check(card, event.pos):
                                flip(card)
                                break

        pygame.display.update()

