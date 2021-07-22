from random import randint
from functions import intInput, sumOfList

POINTS = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


class Round():
    def __init__(self):
        card_deck = self.newDeck()

    def newDeck(self):
        self.card_deck = []
        NEW_DECK = ["2", "3", "4", "5", "6", "7",
                    "8", "9", "10", "J", "Q", "K", "A"]
        for i in range(4):
            self.card_deck.extend(NEW_DECK)

    def randCard(self):
        num = randint(0, len(self.card_deck)-1)
        card = self.card_deck[num]
        del self.card_deck[num]
        return card


class GameParticipant:
    def __init__(self):
        self.cards = []
        self.points = 0

    def takeCards(self, current_round, num=1):
        for i in range(num):
            self.cards.append(current_round.randCard())

    def resetCards(self):
        self.cards = []


class Player(GameParticipant):
    def __init__(self):
        super().__init__()
        print('Welcome to Black Jack.')
        self.money = 0
        self.starting_money = 0
        self.current_bet = 0
        self.another_card = False
        self.lost_round = False

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

    def showCards(self):
        print(f'\nYour cards: {self.cards[:]}')

    def countPoints(self):
        global POINTS
        temp_points_list = []
        ace_count = 0
        for item in self.cards:
            if item == 'A':
                ace_count += 1
            temp_points_list.append(POINTS[item])
        p_points = sumOfList(temp_points_list)
        while p_points > 21 and ace_count > 0:
            p_points -= 10
            ace_count -= 1
        alt_points = p_points
        alt = False
        while ace_count > 0:
            alt_points -= 10
            ace_count -= 1
            alt = True
        self.points = [p_points, alt_points, alt]

    def showPoints(self):
        if not self.points[2]:
            print(f'Your score is: {self.points[0]}.')
        elif self.points[2]:
            print(
                f'Your hand has either {self.points[0]} points or {self.points[1]} points.')

    def showCards(self):
        print(f'Your cards are {self.cards[:]}')

    def showCardsAndPoints(self):
        self.countPoints()
        self.showCards()
        self.showPoints()

    def askForAnotherCard(self):
        answer = input('\nWould you like to have another card? (y/n): ')
        while answer != 'y' and answer != 'n':
            print('Please answer only by entering \'y\' or \'n\'.')
            answer = input('Would you like to have another card? (y/n): ')
        if answer == 'y':
            self.another_card = True
        elif answer == 'n':
            self.another_card = False

    def lostBecauseToManyPoints(self):
        self.money -= self.current_bet
        print('\nUnfortunately you lost this round.')
        if self.money > 0:
            print(f'You got ${self.money} left.')
            print('Good luck in the next round!\n')

        self.lost_round = True

    def wins(self):
        self.money += self.current_bet
        print(f'\nCongratulations! You\'ve won ${self.current_bet}!')
        print(f'You now have ${self.money}.\n')

    def loses(self):
        self.money -= self.current_bet
        print('\nUnfortunately you lost this round.')
        print(f'You\'ve lost ${self.current_bet} in this round.')
        if self.money > 0:
            print(f'You got ${self.money} left.')
            print('\nGood luck next time!\n')

    def showEndResult(self):
        print(
            f'\nYour started with ${self.starting_money} and now have ${self.money}!')
        if self.money > self.starting_money:
            increase_in_percent = round(
                (self.money/self.starting_money - 1) * 100, 2)
            print(
                f'This means you increased your money by ${self.money-self.starting_money}.')
            print(f'That\'s an increase by {increase_in_percent}% !')
        elif self.money < self.starting_money:
            decrease_in_percent = round(
                (1 - self.money/self.starting_money) * 100, 2)
            print(
                f'This means you decreased your money by ${self.starting_money-self.money}.')
            print(f'That\'s an decrease by {decrease_in_percent}%.')


class Dealer(GameParticipant):
    def __init__(self):
        super().__init__()
        self.cards = []

    def countPoints(self):
        temp_points_list = []
        ace_count = 0
        for item in self.cards:
            if item == 'A':
                ace_count += 1
            temp_points_list.append(POINTS[item])
        self.points = sumOfList(temp_points_list)
        while self.points > 21 and ace_count > 0:
            self.points -= 10
            ace_count -= 1
        return self.points

    def showPoints(self):
        print(f'The dealer hand has {self.points} points.')

    def showCards(self):
        if len(self.cards) == 1:
            print(f'The dealer\' card is {self.cards[:]}')
        elif len(self.cards) > 1:
            print(f'The dealer\'s cards are {self.cards[:]}')

    def showCardsAndPoints(self):
        self.countPoints()
        self.showCards()
        self.showPoints()

    def takeEndCards(self, current_round):
        print('\nThe dealer now takes his cards.\n')
        while self.points <= 16:
            self.takeCards(current_round)
            self.countPoints()
