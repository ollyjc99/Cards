import pygame
import random
from PIL import Image
from collections import namedtuple


class Card(object):
    def __init__(self, win, suit, face):
        self.win = win
        self.width = 100
        self.height = self.width * 1.28
        self.x = 0; self.y = 0
        self.suit = suit
        self.colour = self.suit_colour()
        self.face = face

    def suit_colour(self):
        if self.suit == 'spades' or self.suit == 'clubs':
            return 0, 0, 0
        elif self.suit == 'diamonds' or self.suit == 'hearts':
            return 255, 0, 0

    def generate_pattern(self):
        # pos = namedtuple('pos', ['x','y'])
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
            pos = [((self.x + self.width / 2) - 10, (self.y + self.height * 0.25) - 10),
                   ((self.x + self.width / 2) - 10, (self.y + self.height * 0.75) - 10),
                   (mid_x, mid_y)
                   ]
            for i in pos:
                pygame.draw.rect(self.win, self.colour, (i[0], i[1], 20, 20))
        else:
            print('Oops')

    def draw(self):
        pygame.draw.rect(self.win, (255, 255, 255), (self.x, self.y, self.width, self.height))
        # self.generate_pattern()


def main():
    win_width = 800
    win_height = 600
    win = pygame.display.set_mode((win_width, win_height))
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    deck = [Card(win, suit, face) for suit in suits for face in faces]

    grid = [[[x, y] for x in range(66, 734, 100+13)] for y in range(71, 529, 128+35)]
    for row in grid:
        print(row)
        for col in row:
            pygame.draw.rect(win, (225,225,225), (col[0], col[1], 100, 128))

    card = Card(win, 'clubs', '3')
    # card.draw()
    print(card.face, 'of', card.suit)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()