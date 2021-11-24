from random import shuffle
from components.display import display_player, display_dealer 
from components.bet.bet import player_bet
from components.deal import deal_player, deal_dealer
from components.options import player_options, player_stay
from components.decks import create_deck


def start_game():
    """
    This function starts the game.
    """
    deck = create_deck()
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
        if r is False:
            player_stay(player, dealer, deck, player_score, dealer_score, bet)

        display_player(player)
        display_dealer(dealer)


start_game()
