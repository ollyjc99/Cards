import pygame
import random
from PIL import Image
from collections import namedtuple
from pairs import *
from bus import bus
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
        self.win.blit(pygame.transform.scale(self.im, (self.width, self.height)), pos)

    def flip(self):
        if self.flipped:
            return pygame.image.load(self.front)
        else:
            return pygame.image.load(self.back)


def main():
    # Generates Cards
    # pattern_gen.main()

    win_width = 1024
    win_height = 768
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_icon(pygame.image.load('static/img/template/diamonds.png'))

    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [[face, suit] for face in faces for suit in suits]

    # pairs(1280, 720, Card, deck, clock)
    bus(1024, 768, Card, deck, 5, clock)


if __name__ == '__main__':
    pygame.init()
    main()
