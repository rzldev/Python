class Chip :
    def __init__(self, total=100) :
        self.total = total
        self.bet = 0

    def win_bet(self) :
        self.total += self.bet

    def lose_bet(self) :
        self.total -= self.bet

    def take_bet(self) :
        while True :
            try :
                self.bet = int(input('How many chips would you like to bet? '))
                print()
            except :
                print('Sorry, please provide a number')
            else :
                if self.bet > self.total :
                    print('Sorry, you do not have enough chips! You have {} chips'.format(self.total))
                else :
                    break
