import pygame
import random
import time


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


def sandbox(win_width, win_height, deck, clock):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('The Bus')
    win.fill((75, 125, 75))

    deck.draw((round(win_width * .85), round(win_height * .80)))
    setup(win, deck)

    hand = pygame.sprite.Group()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                if event.button == 1:
                    pass

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
        hand.draw(win)
        pygame.display.update()

