import pygame
import time
from threading import Thread


class Deck(object):
    def __init__(self, win, cards):
        self.win = win
        self.x = 0
        self.y = 0
        self.cards = cards
        self.im = pygame.image.load('static/img/template/deck.png')
        self.rect = self.im.get_rect(x=self.x, y=self.y)

    def draw(self, pos=None):
        if pos:
            self.x, self.y = pos

        self.rect = self.im.get_rect(x=self.x, y=self.y)
        self.win.blit(self.im, self.rect)


class Card(object):
    def __init__(self, suit, face):
        self.face = face
        self.suit = suit


class CardSprite(pygame.sprite.Sprite):
    def __init__(self, card):
        pygame.sprite.Sprite.__init__(self)
        self.flipped = False
        self.suit, self.face = card
        self.image = self.flip()
        self.rect = self.image.get_rect()

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
            print(f'{self.card.face} of {self.card.suit}')
            self.card.center = pygame.mouse.get_pos()
            print(self.card.center)
