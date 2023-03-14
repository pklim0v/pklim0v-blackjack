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

    def take_card(self, card, input_face_up=True):
        self.cards.append(Card(card, input_face_up))
        self.calculate_points()

    def calculate_points(self):
        for card in self.cards:
            self.points += card.points

    def print_cards(self):
        players_cards_image = ''

        row_one = '\n'
        row_two = '\n'
        row_three = '\n'
        row_four = '\n'
        row_five = '\n'
        row_six = '\n'
        row_seven = '\n'
        row_eight = '\n'
        row_nine = '\n'
        row_ten = '\n'

        for card in self.cards:
            row_one += '####################     '

            if not card.is_face_up:
                row_two += '#    @@@@@@@@@@    #     '
                row_three += '#      $$$$$$      #     '
                row_four += '#        **        #     '
                row_five += '#     pklim0v\'s    #     '
                row_six += '#     BlackJack    #     '
                row_seven += '#       GAME       #     '
                row_eight += '#        **        #     '
                row_nine += '#      $$$$$$      #     '
                row_ten += '#    @@@@@@@@@@    #     '

            else:
                row_two += '#     pklim0v\'s    #     '
                row_ten += '#     BlackJack    #     '
                if card.name == '10':
                    row_three += '# {name}            {name} #     '.format(name=card.name[:2])
                    row_nine += '# {name}            {name} #     '.format(name=card.name[:2])
                else:
                    row_three += '# {name}              {name} #     '.format(name=card.name[:1])
                    row_nine += '# {name}              {name} #     '.format(name=card.name[:1])

                if card.suit == 'hearts':
                    row_four += '#     ##   ##      #     '
                    row_five += '#    #########     #     '
                    row_six += '#     #######      #     '
                    row_seven += '#      #####       #     '
                    row_eight += '#        #         #     '

                elif card.suit == 'tiles':
                    row_four += '#        #         #     '
                    row_five += '#       ###        #     '
                    row_six += '#     #######      #     '
                    row_seven += '#      #####       #     '
                    row_eight += '#        #         #     '

                elif card.suit == 'pikes':
                    row_four += '#        #         #     '
                    row_five += '#      #####       #     '
                    row_six += '#     #######      #     '
                    row_seven += '#        #         #     '
                    row_eight += '#      #####       #     '

                elif card.suit == 'clovers':
                    row_four += '#        #         #     '
                    row_five += '#        #         #     '
                    row_six += '#    #########     #     '
                    row_seven += '#        #         #     '
                    row_eight += '#        #         #     '


        # total image of player's cards

        players_cards_image = row_one + row_two + row_three + row_four + row_five + row_six + row_seven + row_eight + \
                              row_nine + row_ten + row_one

        return players_cards_image

# class of Card, which have the following attributes:
#
#
#
#

class Card:

    face_down_image = '''
    ####################
    #    @@@@@@@@@@    #
    #      $$$$$$      #
    #        **        #           #           ##   ##               #               # 
    #     pklim0v's    #          ###         #########            #####             #    
    #     BlackJack    #         #####         #######            #######        #########
    #       GAME       #          ###           #####                #               #     
    #        **        #           #              #                #####             # 
    #      $$$$$$      #
    #    @@@@@@@@@@    #
    ####################
    '''
    def __init__(self, card, input_face_up=True):
        self.suit = card[0]
        self.name = card[1][0]
        self.points = card[1][1]
        self.is_face_up = input_face_up


