from .display import display_player, display_dealer
from .deal import *
from .validate import *


def player_options(deck, player, player_score):
    """
    This function allows the player to hit or stay.
    """
    choice = input("Would you like to hit or stay? ")
    print('\n')
    if choice == "hit":
        return True
    else:
        return False


def dealer_options(dealer_score):
    """
    This function allows the dealer to hit or stay.
    """
    if dealer_score < 17:
        return True
    else:
        return False


def player_stay(player, dealer, deck, player_score, dealer_score, bet):
    """
    This function allows the player to stay.
    """
    if dealer_options(dealer_score):
        dealer_score = deal_dealer(deck, dealer, dealer_score)
        display_player(player)
        display_dealer(dealer)
        check_score(player_score, dealer_score, player, dealer, bet)
    else:
        check_score(player_score, dealer_score, player, dealer, bet)
