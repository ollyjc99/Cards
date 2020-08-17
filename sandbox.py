import pygame
import random
import time
from cards import *


def setup(win, deck):
    w, h = win.get_size()

    card_width = round(w*.098)
    card_height = round(h*.167)

    for card in deck.cards:
        card.width = card_width
        card.height = card_height


def card_check(card, pos):
    if card.im.get_rect(x=card.rect.x, y=card.rect.y).collidepoint(pos):
        return True
    else:
        return False


def flip(card):
    card.flipped = not card.flipped
    card.im = card.flip()


def sandbox(w, h, deck, clock):
    win = pygame.display.set_mode((w, h))
    pygame.display.set_caption('The Bus')
    win.fill((75, 125, 75))

    setup(win, deck)

    hand = pygame.sprite.Group()

    running = True
    try:

        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
                    if event.button == 1:
                        if deck.rect.collidepoint(event.pos):
                            if deck.cards:
                                card = deck.cards[0]
                                hand.add(CardSprite((card.suit, card.face)))


                    elif event.button == 2:
                        for card in deck.cards:
                            print(f'{card.face} of {card.suit}')

                    elif event.button == 3:
                        if hand:
                            for card in hand:
                                if card_check(card, event.pos):
                                    flip(card)
                                    break

                        for card in deck.cards:
                            if card_check(card, event.pos):
                                flip(card)
                                break

                    elif event.button == 4:
                        if hand:
                            for card in hand:
                                deck.cards.append(card)
                                hand.remove(0)

            win.fill((75, 125, 75))

            hand.update()

            deck.draw((round(w * .88), round(h * .80)))
            hand.draw(win)
            pygame.display.update()

    except KeyboardInterrupt:
        pass

    except pygame.error:
        pass
