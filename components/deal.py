from random import choice


def deal_player(deck, player, player_score):
    """
    This function deals a card to the player.
    """
    player_card = choice(deck)
    player.append(player_card)
    deck.remove(player_card)

    player_score += player_card.rank_value
    return player_score


def deal_dealer(deck, dealer, dealer_score):
    """
    This function deals a card to the dealer.
    """

    dealer_card = choice(deck)
    dealer.append(dealer_card)
    deck.remove(dealer_card)

    dealer_score += dealer_card.rank_value
    return dealer_score
