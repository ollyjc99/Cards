import os
import pygame
import random
from PIL import Image, ImageDraw, ImageFont
from collections import namedtuple


def pattern_gen(deck):
    card = random.choice(deck)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


def main():
    template = Image.open('img/card_base.png')
    heart = Image.open('img/heart.png')
    a = (6,8)
    b = (80,100)
    fnt = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 20)
    d = ImageDraw.Draw(template)
    d.text(a, "8", font=fnt, fill=(255,0,0))

    png_info = template.info
    template.paste(heart, (6,30), heart)
    template.save('img/test_card.png', **png_info)

    template.show()


if __name__=='__main__':
    main()