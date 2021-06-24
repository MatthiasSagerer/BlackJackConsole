from random import randint
points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

deck = []


def newDeck():
    global deck
    deck = []
    NEW_DECK = ["2", "3", "4", "5", "6", "7",
                "8", "9", "10", "J", "Q", "K", "A"]
    for i in range(4):
        deck.extend(NEW_DECK)


def randCard():
    global deck
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


def itsATie(play):
    print('\nIt\'s a tie!')
    print(f'You got ${play.money} left.')
    print('Good luck in the next round!\n')


def askForNewRound():
    continue_playing = input(
        'Would you like to play another round? (y/n): ')
    while continue_playing != 'y' and continue_playing != 'n':
        print('Please answer only by entering \'y\' or \'n\'.')
        continue_playing = input(
            'Would you like to play another round (y/n): ')
    if continue_playing == 'n':
        return False
    return True


def lostRoundAskForNew():
    print('You have run out of money...')
    another_round = input('Would you like to play again? (y/n): ')
    while another_round != 'y' and another_round != 'n':
        print('Please answer only by entering \'y\' or \'n\'.')
        another_round = input('Would you like to play again? (y/n): ')
    if another_round == 'y':
        return True
    elif another_round == 'n':
        return False


def newLine():
    print('')
