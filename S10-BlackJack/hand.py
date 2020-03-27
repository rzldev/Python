class Hand :
    def __init__(self, values) :
        self.cards = []
        self.value = 0
        self.aces = 0
        self.values = values

    def add_card(self, card) :
        self.cards.append(card)
        self.value += self.values[card.rank]

        if card.rank == 'Ace' :
            self.aces += 1

    def adjust_for_ace(self) :
        while self.value > 21 and self.aces > 0 :
            self.value -= 10
            self.aces -= 1
