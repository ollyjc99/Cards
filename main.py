import pygame
import random
from PIL import Image
from collections import namedtuple
from pairs import *
import pattern_gen


class Card(object):
    def __init__(self, win, width, height, suit, face):
        self.win = win
        self.width = width
        self.height = int(height)
        self.x = 0; self.y = 0
        self.suit = suit
        self.colour = self.suit_colour()
        self.face = face
        self.href = f'img/{self.suit}/{self.face}.png'

    def suit_colour(self):
        if self.suit == 'spades' or self.suit == 'clubs':
            return 0, 0, 0
        elif self.suit == 'diamonds' or self.suit == 'hearts':
            return 255, 0, 0

    def draw(self, pos):
        self.win.blit(pygame.transform.scale(pygame.image.load(self.href), (self.width, self.height)), pos)


def main():
    win_width = 800
    win_height = 600

    card_width = 100
    card_height = int(card_width*1.28)

    win = pygame.display.set_mode((win_width, win_height))

    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    pattern_gen.main()
    deck = [Card(win, card_width, card_height, suit, face) for suit in suits for face in faces]
    card = Card(win, card_width, card_height, 'clubs', '3')
    print(card.face, 'of', card.suit)

    pairs(win, deck)


if __name__ == '__main__':
    main()
