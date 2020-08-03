import pygame
import random
from PIL import Image
from collections import namedtuple
from pairs import *
import pattern_gen


class Card(object):
    def __init__(self, win, width, height, suit, face):
        self.win = win
        self.x = 0; self.y = 0
        self.width = width
        self.height = height
        self.suit = suit
        self.colour = self.suit_colour()
        self.face = face
        self.front = f'static/img/{self.suit}/{self.face}.png'
        self.back = 'static/img/template/card_back.png'
        self.flipped = False
        self.im = self.flip()

    def suit_colour(self):
        if self.suit == 'spades' or self.suit == 'clubs':
            return 0, 0, 0
        elif self.suit == 'diamonds' or self.suit == 'hearts':
            return 255, 0, 0

    def draw(self, pos):
        # self.im = self.flip()
        self.win.blit(pygame.transform.scale(self.im, (self.width, self.height)), pos)

    def flip(self):
        if self.flipped:
            return pygame.image.load(self.front)
        else:
            return pygame.image.load(self.back)

def main():
    win_width = 800
    win_height = 600

    card_width = 100
    card_height = int(card_width*1.28)

    win = pygame.display.set_mode((win_width, win_height))

    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # test = [[face, suit] for face in faces for suit in suits]
    # for face, suit in test:
    #     print(suit, face)

    # Generates Cards
    # pattern_gen.main()
    deck = [Card(win, card_width, card_height, suit, face) for suit in suits for face in faces]

    pairs(win, deck)


if __name__ == '__main__':
    main()
