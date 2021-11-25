def display_player(player):
    """
    This function displays the player's hand in text.
    """
    print("Your hand: ")
    for card in player:
        print(card)
    print('\n')
    display_card(player)


def display_dealer(dealer):
    """
    This function displays the dealer's hand in text.
    """
    print("Dealer's hand: ")
    for card in dealer:
        print(card)
    print('\n')
    display_card(dealer)


def display_card(player):
    """
    This function displays the player's or dealers's graphically.
    """
    s = ""
    for card in player:
        s = s + "\t ________________"
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        if card.rank_value == 10 or card.rank_value == 11:
            s = s + "\t|  {}            |".format(card.rank_value)
        else:
            s = s + "\t|  {}             |".format(card.rank_value)  
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        s = s + "\t|       {}        |".format(card.suit_value)
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in player:
        if card.rank_value == 10 or card.rank_value == 11:
            s = s + "\t|            {}  |".format(card.rank_value)
        else:
            s = s + "\t|            {}   |".format(card.rank_value)
    print(s)

    s = ""
    for card in player:
        s = s + "\t|________________|"
    print(s)

    print()
