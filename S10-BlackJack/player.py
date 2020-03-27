class Player :
    def __init__(self, player, dealer, chips) :
        self.player = player
        self.dealer = dealer
        self.chips = chips

    def player_hit(self, deck) :
        single_card = deck.deal()
        self.player.add_card(single_card)
        self.player.adjust_for_ace()

    def dealer_hit(self, deck) :
        single_card = deck.deal()
        self.dealer.add_card(single_card)
        self.dealer.adjust_for_ace()

    def hit_or_stand(self, deck, playing) :
        while True :
            hs = input('Hit or Stand (enter h or s): ')

            if hs[0].lower() == 'h' :
                self.player_hit(deck)

            elif hs[0].lower() == 's' :
                print('Player choose to stand, Dealer\'s turn')
                playing = False

            else :
                print('Sorry, i did not understand that, please enter h or s only!')
                continue

            break

    def player_busts(self, chips) :
        print('PLAYER BUSTED!')
        chips.lose_bet()

    def player_wins(self, chips) :
        print('PLAYER WINS!')
        chips.win_bet()

    def dealer_busts(self, chips) :
        print('PLAYER WINS! DEALER BUSTED!')
        chips.win_bet()

    def dealer_wins(self, chips) :
        print('DEALER WINS! PLAYER BUSTED!')
        chips.lose_bet()

    def push(self) :
        print('Dealer and Player tie!, PUSH')

    def show_some(self) :
        print('DEALER\'S HAND: ')
        print('One card hidden!')
        print(self.dealer.cards[1])
        print('\n')
        print('PLAYER\'S HAND: ')

        for card in self.player.cards :
            print(card)

    def show_all(self) :
        print('DEALER\'S HAND: ')

        for card in self.dealer.cards :
            print(card)

        print('\n')
        print('PLAYER\'S HAND: ')

        for card in self.player.cards :
            print(card)
