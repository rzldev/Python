from deck import Deck
from hand import Hand
from chip import Chip
from player import Player

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}

playing = True

# ## Call Deck class
# d = Deck(suits, ranks)
#
# ## Show all the cards
# print(d)
#
# print()
#
# ## Random shuffled deck
# d.shuffle()
# print(d)
#
# print()
#
# ## Show a single popup random card
# single_card = d.deal()
# print('Single card: ' + str(single_card))
#
# print()
#
# ## Call Hand class
# h = Hand()
# h.add_card(single_card, values)
# print(h.value)

def start_game(playing) :
    while True :
        print('WELCOME TO BLACKJACK')
        deck = Deck(suits, ranks)
        deck.shuffle()

        player_hand = Hand(values)
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand(values)
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chip()
        player_chips.take_bet()

        player = Player(player_hand, dealer_hand, player_chips.bet)
        player.show_some()

        while playing :
            player.hit_or_stand(deck, player_hand)

            player.show_some()

            if player_hand.value > 21 :
                player.player_busts(player_chips)

            if player_hand.value <= 21 :
                while dealer_hand.value < player_hand.value :
                    player.dealer_hit(deck)

                player.show_all()

                if dealer_hand.value > 21 :
                    player.dealer_busts(player_chips)
                elif dealer_hand.value > player_hand.value :
                    player.dealer_wins(player_chips)
                elif dealer_hand.value < player_hand.value :
                    player.player_wins(player_chips)
                else :
                    player.push()

            print('\nPlayer total chips are at: {}'.format(player_chips.total))

            new_game = input('Would you like to play another game?(y/n) ')

            if new_game.lower() == 'y' :
                playing = True
                continue
            else :
                print('You brings {} chips'.format(player_chips.total))
                break

        break

if __name__ == '__main__' :
    start_game(playing)
