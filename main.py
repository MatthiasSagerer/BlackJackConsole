# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:16:55 2020

@author: Matthias Sagerer
"""
from random import randint
points = {"2":2, "3":3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11} 
def newDeck():
    global deck
    deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    for i in range(2):
        deck.extend(deck)
newDeck()

def randCard():
    num = randint(0,len(deck)-1)
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
        print(f'Your score is: {p_score[0]}.')
    elif score[2]:
        print(f'Your highest possible score is {p_score[0]} and your lowest {p_score[1]}.')
        
def intInput(string):
    invalid_input = True
    while invalid_input:
        try:
            num = int(input(string))
            invalid_input = False
        except:
            print('You have to input an integer.')
    return int(num)

playing = True
while playing:
    money = intInput('Enter the ammount of dollars that you would like to start with: $')
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
                    answer = input('Would you like to have another card? (y/n): ')
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
            continue_playing = input('Would you like to play another round? (y/n): ')
            while continue_playing != 'y' and continue_playing != 'n':
                print('Please answer only by entering \'y\' or \'n\'.')
                continue_playing = input('Would you like to play another round (y/n): ')
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

# TODO: writing cleaner code!!