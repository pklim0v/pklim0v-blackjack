from blackjack import deck

def print_privet(name):
    print('Hi, {name}!'.format(name=name))

def get_user_name():
    user_name = input('Hello, friend! Please enter your name: ')
    return user_name


if __name__ == '__main__':
    print_privet(get_user_name())
    print(deck.generate_deck())


