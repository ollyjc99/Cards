import pygame
import random
from PIL import Image
from collections import namedtuple
from pairs import *
from pattern_gen import *


class Card(object):
    def __init__(self, win, width, height, suit, face, href='img/hearts/ace.png'):
        self.win = win
        self.width = width
        self.height = int(height)
        self.x = 0; self.y = 0
        self.suit = suit
        self.colour = self.suit_colour()
        self.face = face
        self.href = href

    def suit_colour(self):
        if self.suit == 'spades' or self.suit == 'clubs':
            return 0, 0, 0
        elif self.suit == 'diamonds' or self.suit == 'hearts':
            return 255, 0, 0

    def draw(self, pos):
        self.win.blit(pygame.transform.scale(pygame.image.load(self.href), (self.width, self.height)), pos)

    def generate_pattern(self):

        mid_x = (self.x + self.width / 2) - 10
        mid_y = (self.y + self.height / 2) - 10

        if self.face == 'Ace':
            pygame.draw.rect(self.win, self.colour, (mid_x, mid_y, 20, 20))

        elif self.face == '2':
            pos = [((self.x+self.width/2)-10, (self.y+self.height*0.25)-10),
                   ((self.x + self.width / 2) - 10, (self.y + self.height * 0.75)-10)
                   ]
            for i in pos:
                pygame.draw.rect(self.win, self.colour, (i[0], i[1], 20, 20))

        elif self.face == '3':
            pos = [(mid_x, (self.y + self.height * 0.25) - 10),
                   (mid_x, (self.y + self.height * 0.75) - 10),
                   (mid_x, mid_y)
                   ]
            for i in pos:
                pygame.draw.rect(self.win, self.colour, (i[0], i[1], 20, 20))
        else:
            print('Oops')


def main():
    win_width = 800
    win_height = 600

    card_width = 100
    card_height = int(card_width*1.28)

    win = pygame.display.set_mode((win_width, win_height))

    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    deck = [Card(win, card_width, card_height, suit, face) for suit in suits for face in faces]
    card = Card(win, card_width, card_height, 'clubs', '3')
    print(card.face, 'of', card.suit)

    # pairs(win, deck)
    pattern_gen(deck)


if __name__ == '__main__':
    main()
