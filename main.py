# Blackjack Midterm Project
# 22/11/2021

# Rules for Blackjack:
# - The game begins with the player placing a bet.
# - The player is dealt two cards.
# - The dealer is dealt two cards.
# - The player is given the option to hit or stay.
# - The dealer will hit if the dealer's score is less than 17.
# - The dealer will stay if the dealer's score is 17 or more.
# - The player wins if their score is higher than the dealer's.
# - The dealer wins if their score is higher than the player's.
# - The player wins if their score is 21.
# - The dealer wins if their score is 21.
# - The player wins if their score is higher than the dealer's and less than 21.
# - The dealer wins if their score is higher than the player's and less than 21.
# - The game is a draw if the player and dealer's scores are equal and both are 21.

# TODO:
# - Handle aces properly
# - Handle wagers
# - Handle save files
# - Handle player quitting without saving
# - Graphically display cards
# - Allow player to enter a new game


from random import shuffle
from components.display import display_player, display_dealer 
from components.bet.bet import player_bet
from components.deal import deal_player, deal_dealer
from components.options import player_options, dealer_options, player_stay
from components.validate import check_score
from components.decks import Deck

# Game Loop

def start_game():
    """
    This function starts the game.
    """
    deck = Deck()
    shuffle(deck)

    player = []
    dealer = []

    player_score = 0
    dealer_score = 0

    bet = player_bet()

    # Deal cards to player and dealer.
    player_score = deal_player(deck, player, player_score)
    player_score = deal_player(deck, player, player_score)

    dealer_score = deal_dealer(deck, dealer, dealer_score)
    dealer_score = deal_dealer(deck, dealer, dealer_score)

    # If double aces, change first ace to 1.
    if player[0].rank_value == 11 and player[1].rank_value == 11:
        player[0].rank_value = 1
        player_score -= 10
    if dealer[0].rank_value == 11 and dealer[1].rank_value == 11:
        dealer[0].rank_value = 1
        dealer_score -= 10

    display_player(player)
    display_dealer(dealer)

    while True:
        r = player_options(deck, player, player_score)
        if r:
            player_score = deal_player(deck, player, player_score)
        if r == False:
            player_stay(player, dealer, deck, player_score, dealer_score)

        display_player(player)
        display_dealer(dealer)


start_game()
