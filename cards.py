import pygame


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


class Card(pygame.sprite.Sprite):
    def __init__(self, win, width, height, suit, face):
        pygame.sprite.Sprite.__init__(self)
        self.flipped = False
        self.image = self.flip()
        self.width = width
        self.height = height
        self.suit = suit
        self.face = face
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def flip(self):
        if self.flipped:
            return pygame.image.load(f'static/img/{self.suit}/{self.face}.png')
        else:
            return pygame.image.load('static/img/template/card_back.png')
