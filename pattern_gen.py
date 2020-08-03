import os
import pygame
import random
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from collections import namedtuple


def main():
    faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['hearts','diamonds','spades','clubs']

    for suit in suits:
        for face in faces:
            template = Image.open('static/img/template/card_base.png')
            w, h = template.size
            png_info = template.info
            icon = Image.open(f'static/img/template/{suit}.png')
            small_icon = icon.resize((9, 9))
            template.paste(small_icon, (8,30))
            fnt = ImageFont.truetype("static/font/Arial.ttf", 20)
            d = ImageDraw.Draw(template)

            if suit == 'hearts' or suit == 'diamonds':
                colour = (255,0,0)
            else:
                colour = (0,0,0)
            if face == 'A':
                d.text((6,8), face, font=fnt, fill=colour)
            elif face == '10':
                d.text((2,8), '1', font=fnt, fill=colour)
                d.text((11, 8), '0', font=fnt, fill=colour)
            elif face == 'Q':
                d.text((5,8), face, font=fnt, fill=colour)
            elif face == 'K':
                d.text((6,8), face, font=fnt, fill=colour)
            else:
                d.text((7,8), face, font=fnt, fill=colour)

            region = template.crop((0,0, w, h/2))
            region = region.transpose(Image.ROTATE_180)
            template.paste(region, (0,64))

            gen_pattern(template, icon, face, d, colour)

            template.save(f'static/img/{suit}/{face}.png', **png_info)


def gen_pattern(card, icon, face, d, colour):
    x = int(card.width/2)
    y = int(card.height/2)
    fnt = ImageFont.truetype("static/font/Backslash-RpJol.otf", 42)
    if face == 'A':
        enhancer = ImageEnhance.Sharpness(icon)
        enhancer.enhance(2.0)
        mid_point = (int(x-icon.width/2), int(y-icon.height/2))
        card.paste(icon, mid_point)

    elif face == 'J':
        d.text((x-5,y-20), 'J', font=fnt, fill=colour)

    elif face == 'Q':
        d.text((x-15, y - 20), 'Q', font=fnt, fill=colour)

    elif face == 'K':
        d.text((x-13, y - 20), 'K', font=fnt, fill=colour)

    else:
        icon = icon.resize((15, 15))
        x = int(card.width / 2 - icon.width / 2)
        y = int(card.height / 2 - icon.width / 2)
        points = get_points(face, (x, y))
        if points:
            for point in points:
                card.paste(icon, point)


def get_points(face, mid_point):
    points = []
    x, y = mid_point
    if face == '2':
        points = [
            (x, int(y/2)),
            (x, int(y*1.5))
        ]

    elif face == '3':
        points = [
            (x, int(y / 2)),
            (x, y),
            (x, int(y * 1.5))
        ]

    elif face == '4':
        points = [
            (int(x*.5), int(y / 2)),
            (int(x*1.5), int(y / 2)),
            (int(x*.5), int(y * 1.5)),
            (int(x*1.5), int(y * 1.5))
        ]

    elif face == '5':
        points = [
            (int(x * .5), int(y / 2)),
            (int(x * 1.5), int(y / 2)),
            (x, y),
            (int(x * .5), int(y * 1.5)),
            (int(x * 1.5), int(y * 1.5))
        ]

    elif face == '6':
        points = [
            (int(x * .5), int(y / 2)),
            (int(x * 1.5), int(y / 2)),
            (int(x * .5), y),
            (int(x * 1.5), y),
            (int(x * .5), int(y * 1.5)),
            (int(x * 1.5), int(y * 1.5))
        ]

    elif face == '7':
        points = [
            (int(x * .5), int(y / 2)),
            (int(x * 1.5), int(y / 2)),
            (x, int(y*.75)),
            (int(x * .5), y),
            (int(x * 1.5), y),
            (int(x * .5), int(y * 1.5)),
            (int(x * 1.5), int(y * 1.5))
        ]

    elif face == '8':
        points = [
            (int(x * .5), int(y / 2)),
            (int(x * 1.5), int(y / 2)),
            (x, int(y * .75)),
            (int(x * .5), y),
            (int(x * 1.5), y),
            (x, int(y * 1.25)),
            (int(x * .5), int(y * 1.5)),
            (int(x * 1.5), int(y * 1.5))
        ]

    elif face == '9':
        points = [
            (int(x * .5), int(y / 2.3)),
            (int(x * 1.5), int(y / 2.3)),
            (x, int(y / 1.5)),
            (int(x * .5), int(y / 1.15)),
            (int(x * 1.5), int(y / 1.15)),
            (int(x * .5), int(y * 1.3)),
            (int(x * 1.5), int(y * 1.3)),
            (int(x * .5), int(y * 1.7)),
            (int(x * 1.5), int(y * 1.7))
        ]

    elif face == '10':
        points = [
            (int(x * .5), int(y / 2.3)),
            (int(x * 1.5), int(y / 2.3)),
            (x, int(y / 1.5)),
            (x, int(y * 1.5)),
            (int(x * .5), int(y / 1.15)),
            (int(x * 1.5), int(y / 1.15)),
            (int(x * .5), int(y * 1.3)),
            (int(x * 1.5), int(y * 1.3)),
            (int(x * .5), int(y * 1.7)),
            (int(x * 1.5), int(y * 1.7))
        ]

    return points


if __name__ == '__main__':
    main()
