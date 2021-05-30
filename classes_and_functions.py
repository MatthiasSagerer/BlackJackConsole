from random import randint
points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


def newDeck():
    global deck
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for i in range(2):
        deck.extend(deck)


def randCard():
    num = randint(0, len(deck)-1)
    card = deck[num]
    del deck[num]
    return card


def sumOfList(list):
    sum = 0
    for num in list:
        sum += num
    return sum


def countPlayerPoints(list):
    global points
    player_points = []
    ace_count = 0
    for item in list:
        if item == 'A':
            ace_count += 1
        player_points.append(points[item])
    p_points = sumOfList(player_points)
    while p_points > 21 and ace_count > 0:
        p_points -= 10
        ace_count -= 1
    alt_points = p_points
    alt = False
    while ace_count > 0:
        alt_points -= 10
        ace_count -= 1
        alt = True
    all_points = [p_points, alt_points, alt]
    return all_points


def countDealerPoints(list):
    global points
    dealer_points = []
    ace_count = 0
    for item in list:
        if item == 'A':
            ace_count += 1
        dealer_points.append(points[item])
    d_points = sumOfList(dealer_points)
    while d_points > 21 and ace_count > 0:
        d_points -= 10
        ace_count -= 1
    return d_points


def displayPlayerScore(score):
    if not score[2]:
        print(f'Your score is: {score[0]}.')
    elif score[2]:
        print(
            f'Your highest possible score is {score[0]} and your lowest {score[1]}.')


def intInput(string):
    invalid_input = True
    while invalid_input:
        try:
            num = int(input(string))
            invalid_input = False
        except:
            print('You have to input an integer.')
    return int(num)


class Player:
    def __init__(self):
        print('New Player has been created.')
        self.money = 0
        self.starting_money = 0
        current_bet = 0

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
        
    # TODO methods:
    #   - take card
    #   - countPoints
    #   - 


class Dealer:
    def __init__(self):
        print('New Dealer has been created.')

# TODO: dealer class
#       - attributes: cards
#       - methods: new cards


# TODO: playerclass:
#       - attributes: cards
#       - methods: new cards
