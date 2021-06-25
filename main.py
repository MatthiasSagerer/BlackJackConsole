# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:16:55 2020

@author: Matthias Sagerer
"""
from functions import newLine, lostRoundAskForNew,  itsATie, askForNewRound
from classes import Player, Dealer, Round


def blackJackConsole():
    playing = True
    while playing:
        dealer = Dealer()
        player = Player()

        player.selectStartingAmount()

        lap = True

        while player.money > 0 and lap == True:
            player.lost_round = False

            round = Round()

            dealer.resetCards()
            player.resetCards()

            player.makeABet()

            newLine()

            player.takeCards(round, num=2)
            dealer.takeCards(round)

            dealer.showCardsAndPoints()
            player.showCardsAndPoints()

            player.askForAnotherCard()

            while player.another_card:
                player.takeCards(round)

                dealer.showCardsAndPoints()
                player.showCardsAndPoints()

                player.another_card = False
                if player.points[0] > 21:
                    player.lostBecauseToManyPoints()
                else:
                    player.askForAnotherCard()
                    newLine()
            if not player.lost_round:
                dealer.takeEndCards(round)

                dealer.showCardsAndPoints()
                player.showCardsAndPoints()

                if player.points[0] > dealer.points or dealer.points > 21:
                    player.wins()
                elif player.points[0] < dealer.points:
                    player.loses()
                elif player.points[0] == dealer.points:
                    itsATie(player)
            if player.money > 0:
                lap = askForNewRound()
        if not lap:
            player.showEndResult()
            playing = False
        else:
            playing = lostRoundAskForNew()
    print('\nThank you for playing. See you next time!')
    
    input("Press Enter to exit..")


if __name__ == "__main__":
    blackJackConsole()
