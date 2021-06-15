# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:16:55 2020

@author: Matthias Sagerer
"""
from functions import lostRoundAskForNew, points, newDeck, randCard, countDealerPoints, countPlayerPoints, displayPlayerScore, intInput, itsATie, askForNewRound
from classes import Player, Dealer


def blackJackwithoutClasses():
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
            # ask for another card
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
                    answer = input(
                        'Would you like to have another card? (y/n): ')
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
                    print('\nUnfortunately you lost this round.')
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
            print(
                f'\nYour started with ${starting_money} and now have ${money}!')
            playing = False
        else:
            print('You have run out of money...')
            another_round = input('Would you like to play again? (y/n): ')
            while another_round != 'y' and another_round != 'n':
                print('Please answer only by entering \'y\' or \'n\'.')
                another_round = input(' Would you like to play again? (y/n): ')
            if another_round == 'y':
                pass
            elif another_round == 'n':
                playing = False
    print('\nThank you for playing. See you next time!')


def blackJackConsole():
    playing = True
    while playing:
        dealer = Dealer()
        player = Player()

        newDeck()
        player.selectStartingAmount()

        lap = True

        while player.money > 0 and lap == True:
            player.lost_round = False

            player.makeABet()

            player.takeCards(2)
            dealer.takeCards()

            player.countPoints()
            dealer.countPoints()

            dealer.showCardsAndPoints()
            player.showCardsAndPoints()

            player.askForAnotherCard()

            while player.another_card:
                player.takeCards()
                player.countPoints()

                dealer.showCardsAndPoints()
                player.showCardsAndPoints()

                if player.points[0] > 21:
                    player.lostBecauseToManyPoints()
                else:
                    player.askForAnotherCard()
            if not player.lost_round:
                dealer.takeEndCards()

                dealer.showCardsAndPoints()
                player.showCardsAndPoints()

                if player.points[0] > dealer.points or dealer.points > 21:
                    player.wins()
                elif player.points[0] < dealer.points:
                    player.loses()
                elif player.points[0] == dealer.points:
                    itsATie(player)
            newDeck()
            if player.money > 0:
                lap = askForNewRound()
        if not lap:
            player.showEndResult
            playing = False
        else:
            playing = lostRoundAskForNew()
    print('\nThank you for playing. See you next time!')


if __name__ == "__main__":
    blackJackwithoutClasses()
    # blackJackConsole()

# TODO: When class implementation is finished:
#           - test new implementation
#           - DELETE ORIGINAL CODE!
