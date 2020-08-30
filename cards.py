import pygame
import time
from threading import Thread


class Deck(object):
    def __init__(self, win, cards):
        self.win = win
        self.x = 0
        self.y = 0
        self.cards = cards
        self.image = pygame.image.load('static/img/template/deck.png')
        self.rect = self.image.get_rect(x=self.x, y=self.y)

    def __str__(self):
        return f'Deck of {len(self.cards)} cards'

    def draw(self, pos=None):
        if pos:
            self.x, self.y = pos

        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.win.blit(self.image, self.rect)


class Card(pygame.sprite.Sprite):
    def __init__(self, suit, face):
        pygame.sprite.Sprite.__init__(self)
        self.flipped = False
        self.suit = suit
        self.face = face
        self.image = self.flip()
        self.rect = self.image.get_rect()

    def __str__(self):
        return f'{self.face} of {self.suit}'

    def update(self):
        pass

    def flip(self):
        if self.flipped:
            return pygame.image.load(f'static/img/{self.suit}/{self.face}.png')
        else:
            return pygame.image.load('static/img/template/card_back.png')


class DragCard(Thread):
    def __init__(self, card):
        Thread.__init__(self)
        self.daemon = True
        self.card = card
        self.running = True
        self.start()

    def run(self):
        while self.running:
            self.card.center = pygame.mouse.get_pos()
