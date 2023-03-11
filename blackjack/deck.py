# This file creates the  list  which is the deck of cards
from random import randint


suits = ['hearts', 'tiles', 'clovers', 'pikes']

ranks = [
    ['2', 2],
    ['3', 3],
    ['4', 4],
    ['5', 5],
    ['6', 6],
    ['7', 7],
    ['8', 8],
    ['9', 9],
    ['10', 10],
    ['Jack', 2],
    ['Queen', 3],
    ['King', 4],
    ['Ace', 11]
]

def generate_deck():
    generated_deck = []

    for suit in suits:
        for rank in ranks:
            generated_deck.append([suit, rank])

    mixed_deck_index = []

    while len(mixed_deck_index) < len(generated_deck):
        random_deck_index = randint(0, 51)
        if random_deck_index not in mixed_deck_index:
            mixed_deck_index.append(random_deck_index)

    mixed_deck = []

    for index in mixed_deck_index:
        mixed_deck.append(generated_deck[index])

    return mixed_deck

