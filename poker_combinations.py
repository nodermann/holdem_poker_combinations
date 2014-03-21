__author__ = 'Lucian'
from const import values, fibonacci_weight

# intel quad core i7 3770k, average speed of check 56000 combinations of cards per second
# For proper operation of these methods need to sort descending cards (method sort_high_to_low into sort.py)
# No checks for invalid or missing card, you should take care of this yourself
# To get the name of the combination, use the get_combo_name

fib = dict(zip(values, fibonacci_weight))


def weak_royal_flush(cards):
    if len(cards) == 5:
        if cards[0][0] == 'A' and cards[1][0] == \
                'K' and cards[2][0] == 'Q' and cards[3][0] == 'J' and cards[4][0] == 'T':
            return True
    return False


def weak_straight_flush(cards):
    if weak_flush(cards) and weak_straight(cards):
        return True
    return False


def weak_four_of_kind(cards):
    if len(cards) == 5:
        if cards[0][0] == cards[1][0] and cards[0][0] == cards[2][0] and cards[0][0] == cards[3][0]:
            return True
        if cards[4][0] == cards[1][0] and cards[4][0] == cards[2][0] and cards[4][0] == cards[3][0]:
            return True
    return False


def weak_full_house(cards):
    if len(cards) == 5:
        if cards[0][0] == cards[1][0]:
            if cards[2][0] == cards[3][0] and cards[2][0] == cards[4][0]:
                return True
        if cards[0][0] == cards[1][0] and cards[0][0] == cards[2][0]:
            if cards[3][0] == cards[4][0]:
                return True
    return False


def weak_flush(cards):
    if len(cards) == 5:
        native_color = cards[0][1]
        for i, card in enumerate(cards):
            if i == 0:
                continue
            if card[1] != native_color:
                return False
    else:
        return False
    return True


def weak_straight(cards):
    if len(cards) == 5:
        if cards[0][0] == 'A':
            if cards[1][0] == '5' and cards[2][0] == '4' and cards[3][0] == '3' and cards[4][0] == '2':
                return True
        else:
            key = int(fib[cards[0][0]]) + int(fib[cards[1][0]])
            key += int(fib[cards[1][0]])
            key += int(fib[cards[2][0]])
            key += int(fib[cards[3][0]])
            key += int(fib[cards[4][0]])
            if str(key) in fibonacci_weight:
                return True
    return False


def weak_three_of_kind(cards):
    if len(cards) == 3:
        if cards[0][0] == cards[1][0] and cards[0][0] == cards[2][0]:
            return True
    if len(cards) == 5:
        if cards[0][0] == cards[1][0] and cards[0][0] == cards[2][0]:
            return True
        if cards[1][0] == cards[2][0] and cards[1][0] == cards[3][0]:
            return True
        if cards[2][0] == cards[3][0] and cards[2][0] == cards[4][0]:
            return True
    return False


def weak_two_pair(cards):
    if len(cards) == 5:
        if cards[0][0] == cards[1][0] and cards[2][0] == cards[3][0]:
            return True
        if cards[1][0] == cards[2][0] and cards[3][0] == cards[4][0]:
            return True
        if cards[0][0] == cards[1][0] and cards[3][0] == cards[4][0]:
            return True
    return False


def weak_pair(cards):
    if len(cards) == 3:
        if cards[0][0] == cards[1][0] or cards[1][0] == cards[2][0]:
            return True
    if len(cards) == 5:
        if cards[0][0] == cards[1][0] or cards[1][0] == cards[2][0] or cards[2][0] == cards[3][0] or cards[3][0] == cards[4][0]:
            return True
    return False


def weak_high_card(cards):
    if len(cards) == 3 or len(cards) == 5:
        if cards[0][0] != cards[1][0]:
            return True
    return False


def get_combo_name(cards):
    if len(cards) == 3:
        if weak_three_of_kind(cards):
            return 'Three of kind'
        elif weak_pair(cards):
            return 'Pair'
        elif weak_high_card(cards):
            return 'High card'
    if len(cards) == 5:
        if weak_flush(cards):
            if weak_royal_flush(cards):
                return 'Royal flush'
            elif weak_straight_flush(cards):
                return 'Straight flush'
            return 'Flush'
        else:
            if weak_four_of_kind(cards):
                return 'Four of kind'
            elif weak_full_house(cards):
                return 'Full house'
            elif weak_straight(cards):
                return 'Straight'
            elif weak_three_of_kind(cards):
                return 'Three of kind'
            elif weak_two_pair(cards):
                return 'Two pair'
            elif weak_pair(cards):
                return 'Pair'
            elif weak_high_card(cards):
                return 'High card'
    return 'No match ' + str(cards)