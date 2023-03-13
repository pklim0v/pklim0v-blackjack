from blackjack import deck
from blackjack.classes import Player, Card


def print_greeting():
    print('Welcome to pklimov\'s BlackJack text game!')


def setup_players():

    players_quantity = 0.1

    while players_quantity > 7 or players_quantity < 2:
        players_quantity = 0.1
        while type(players_quantity) is not int:
            try:
                players_quantity = int(input('Please specify the quantity of players (2-7): '))
            except ValueError:
                print('Please note that the quantity of players must be Integer!')
        if players_quantity > 7 or players_quantity < 2:
            print('Please enter the number from 2 to 7 inclusive!')

    print('\nGreat, so, let\'s get to know each other!')
    players = []
    for player in range(0, players_quantity):
        player_name = input('\nPlayer {number}, please tell us your name: '.
                            format(number=player + 1))
        players.append(Player(player_name))
        print('\nIt is nice to meet you, {name}! But let\'s go on.'.format(name=players[player].name))

    return players


if __name__ == '__main__':
    print_greeting()
    players = setup_players()
    deck = deck.generate_deck()
    print(players)
    print(deck)
