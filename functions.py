def sumOfList(list):
    sum = 0
    for num in list:
        sum += num
    return sum


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
