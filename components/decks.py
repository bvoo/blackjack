class Card:
    """
    This class creates a card.
    """

    def __init__(self, suit, suit_value, rank, rank_value):
        self.suit = suit
        self.suit_value = suit_value
        self.rank = rank
        self.rank_value = rank_value

    def __str__(self):
        return self.rank + " of " + self.suit


def create_deck():
    """
    This function creates a deck of cards.
    """
    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    suits_values = ["\u2661", "\u2662", "\u2667", "\u2664"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
    ranks_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for suit in range(len(suits)):
        for rank in ranks:
            card = Card(suits[suit], suits_values[suit],
                        rank, ranks_values[ranks.index(rank)])

            deck.append(card)
    return deck
