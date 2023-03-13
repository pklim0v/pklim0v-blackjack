# class of Player, which have the following attributes:
#
#
#
#

class Player:
    def __init__(self, input_name):
        self.name = input_name
        self.cards = []


# class of Card, which have the following attributes:
#
#
#
#

class Card:
    def __init__(self, card):
        self.suit = card[0]
        self.name = card[1][0]
        self.points = card[1][1]


