def check_score(player_score, dealer_score):
    """
    This function checks the score of the player and dealer.
    """
    print(f'Player score: {player_score}\nDealer score: {dealer_score}')
    if player_score > 21:
        print("You busted!")
        exit()
    elif dealer_score > 21:
        print("Dealer busted!")
        exit()
    elif player_score > dealer_score:
        print("You Win!")
        exit()
    elif dealer_score > player_score:
        print("Dealer Wins!")
        exit()
    elif dealer_score == player_score:
        print("It's a draw!")
        exit()
    else:
        print("big problem bucko")
        return False
