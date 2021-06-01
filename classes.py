from functions import intInput, randCard

class GameParticipant:
    def __init__(self):
        print('A new game participant has been created.')
        self.cards = []

    def takeACard(self):
        self.cards.append(randCard())


class Player(GameParticipant):
    def __init__(self):
        super().__init__()
        print('New Player has been created.')
        self.money = 0
        self.starting_money = 0
        self.current_bet = 0

    def selectStartingAmount(self):
        self.money = intInput(
            'Enter the amount of dollars that you would like to start with: $')
        print(f'You will start with ${self.money}.')
        self.starting_money = self.money

    def makeABet(self):
        self.current_bet = intInput('Your bet in this round: $')
        while self.current_bet < 1:
            print('You have to bet at least 1$.')
            self.current_bet = intInput('Your bet in this round: $')
        while self.current_bet > self.money:
            print(f'You only have ${self.money}!')
            self.current_bet = intInput('Your bet in this round: $')


class Dealer:
    def __init__(self):
        print('New Dealer has been created.')
        self.cards = []



# for debugging.   TODO: DELETE BEFORE FINISHING THE CODE !!
if False:
    mario = Player()
    print(deck)
    newDeck()
    mario.takeACard()
    print(mario.cards)