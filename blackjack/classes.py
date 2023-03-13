# class of Player, which have the following attributes:
#
#
#
#

class Player:
    def __init__(self, input_name):
        self.name = input_name
        self.cards = []
        self.points = 0

    def take_card(self, card):
        self.cards.append(Card(card))
        self.calculate_points()

    def calculate_points(self):
        for card in self.cards:
            self.points += card.points

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


