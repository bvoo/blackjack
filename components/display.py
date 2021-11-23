def display_player(player):
    """
    This function displays the player's hand.
    """
    print("Your hand: ")
    for card in player:
        print(card)
    print('\n')


def display_dealer(dealer):
    """
    This function displays the dealer's hand.
    """
    print("Dealer's hand: ")
    for card in dealer:
        print(card)
    print('\n')
