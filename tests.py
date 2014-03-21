__author__ = 'Lucian'
from poker_combinations import get_combo_name
from sort import sort_high_to_low, sort_by_color
from const import values, colors, color_names
import time


def get_deck():
    deck = []
    for i, color in enumerate(colors):
        for value in list(reversed(values)):
            deck.append(value + color)
        print color_names[i]
        print " ".join(deck[i * 13:len(deck)])
    return deck


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "per %f" % (time.time()-t)
        return res

    return tmp


@timer
def test_get_combo_name():
    sample_cards = ["AS QS TS JS KS", "AC JC TC QC KC", "7C 6C TC 8C 9C", "7D 4D 5D 3D 6D",
                    "3H 4H 5H AH 2H", "9H JD 9S 9C 9D", "9H 5S 9S 9C 9D", "9H QS QD QC 9D",
                    "QH 3S QD QC 3D", "JS 2S 4S KS 7S", "JC 2C QC 5C 7C", "8C 2C QC 5C 7C",
                    "8C 2C QC 5C 6C", "7C 6S 5D 8H 9C", "2D 4C 5S 3D 6H", "3H 4H 5D AD 2S",
                    "5H 4C QD QC QS", "5H TH 6D TC TS", "5H TH 4D TC TS", "5H TH 3D TC TS",
                    "9H KH 9D KC 2S", "4D 4H JD JH AC", "4D 4H JD JH TS", "AD 4H JD 7H AS",
                    "AD TH TD 7H 8S", "6D TH TD 4H 5S", "6D TH TD 4H 3S", "6D TH TD 4H 2S",
                    "6D AH TD 4H 2S", "8D 5H 7D JH 2S", "8D 5H 6D JH 2S", "8D 4H 6D JH 2S"]
    for card_set in sample_cards:
        cards = card_set.split(" ")
        cards = sort_high_to_low(cards)
        print str(cards) + ' ' + get_combo_name(cards)


def test_sort_by_color():
    cards = "5H 4C QD QC QS".split(" ")
    print sort_by_color(cards)


def test_sort_high_to_low():
    cards = "8D 5H 6D JH 2S".split(" ")
    print sort_high_to_low(cards)


if __name__ == "__main__":
    #test_sort_by_color()
    #test_sort_high_to_low()
    #get_deck()
    test_get_combo_name()