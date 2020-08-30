def card_check(card, pos):
    if card.image.get_rect(x=card.rect.x, y=card.rect.y).collidepoint(pos):
        return True
    else:
        return False


def flip(card):
    card.flipped = not card.flipped
    card.image = card.flip()
