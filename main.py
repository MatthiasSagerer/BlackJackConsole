# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:16:55 2020

@author: Matthias Sagerer
"""
from classes_and_functions import points, newDeck, randCard, sumOfList, countDealerPoints, countPlayerPoints, displayPlayerScore, intInput
from classes_and_functions import Player, Dealer
newDeck()

playing = True
while playing:
    money = intInput(
        'Enter the amount of dollars that you would like to start with: $')
    print(f'You will start with ${money}.')
    starting_money = money
    lap = True
    while money > 0 and lap == True:
        bet = intInput('Your bet in this round: $')
        while bet < 1:
            print('You have to bet at least 1$.')
            bet = intInput('Your bet in this round: $')
        while bet > money:
            print(f'You only have ${money}!')
            bet = intInput('Your bet in this round: $')
        player_cards = []
        dealer_cards = []
        dealer_cards.append(randCard())
        player_cards.append(randCard())
        player_cards.append(randCard())
        p_score = countPlayerPoints(player_cards)
        d_score = countDealerPoints(dealer_cards)
        print(f'\nThe dealer\'s card is: {dealer_cards[:]}.')
        print(f'The dealer\'s score is: {d_score}.')
        print(f'\nYour cards: {player_cards[:]}')
        displayPlayerScore(p_score)
        answer = input('Would you like to have another card? (y/n): ')
        while answer != 'y' and answer != 'n':
            print('Please answer only by entering \'y\' or \'n\'.')
            answer = input('Would you like to have another card? (y/n): ')
        while answer == "y":
            player_cards.append(randCard())
            p_score = countPlayerPoints(player_cards)
            print(f'\nThe dealer\'s card is: {dealer_cards[:]}')
            print(f'The dealer\'s score is: {d_score}.')
            print(f'\nYour cards: {player_cards[:]}')
            displayPlayerScore(p_score)
            if p_score[0] > 21:
                money -= bet
                print('\nUnfortunately you lost this round')
                print(f'You got ${money} left.')
                print('\nGood luck in the next round!')
                answer = 'lost'
            else:
                answer = input('Would you like to have another card? (y/n): ')
                while answer != 'y' and answer != 'n':
                    print('Please answer only by entering \'y\' or \'n\'.')
                    answer = input(
                        'Would you like to have another card? (y/n): ')
        if answer != 'lost':
            print('\nThe dealer now takes his cards.\n')
            while d_score <= 16:
                dealer_cards.append(randCard())
                d_score = countDealerPoints(dealer_cards)
            print(f'\nThe dealer\'s cards are: {dealer_cards[:]}')
            print(f'The dealer\'s score is: {d_score}.')
            print(f'\nYour cards: {player_cards[:]}')
            displayPlayerScore(p_score)
            if p_score[1] > d_score or d_score > 21:
                money += bet
                print(f'\nCongratulations! You\'ve won ${bet}!')
                print(f'You now have ${money}')
            elif p_score[0] < d_score:
                money -= bet
                print('\nUnfortunately you lost this round')
                print(f'You got ${money} left.')
                print('\nGood luck in the next round!')
            elif p_score[0] == d_score:
                print('It\'s a tie!')
                print(f'You got ${money} left.')
                print('Good luck in the next round!')
        newDeck()
        if money > 0:
            continue_playing = input(
                'Would you like to play another round? (y/n): ')
            while continue_playing != 'y' and continue_playing != 'n':
                print('Please answer only by entering \'y\' or \'n\'.')
                continue_playing = input(
                    'Would you like to play another round (y/n): ')
            if continue_playing == 'n':
                lap = False
    if not lap:
        print(f'\nYour started with ${starting_money} and now have ${money}!')
        playing = False
    else:
        print('You have run out of money...')
        another_round = input('Would you like to play again? (y/n): ')
        while another_round != 'y' and another_round != 'n':
            print('Please answer only by entering \'y\' or \'n\'.')
            another_round = input('Would you like to play again? (y/n): ')
        if another_round == 'y':
            pass
        elif another_round == 'n':
            playing = False
print('\nThank you for playing. See you next time!')

# TODO: writing cleaner code:
#       - Dealer Class
#       - Player Class
#       - parent Class for Dealer and Player with inheritance
