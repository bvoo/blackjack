def check_score(player_score, dealer_score, player, dealer):
    """
    This function checks the score of the player and dealer.
    """
    print(f'Player score: {player_score}\nDealer score: {dealer_score}')
    if player_score > 21:
        # Deal with aces by looping through all cards if over 21.
        for card in player:
            if card.rank_value == 11:
                print(f'\nReducing Ace\n')
                card.rank_value = 1
                player_score -= 10
                check_score(player_score, dealer_score, player, dealer)
        if player_score > 21:
            print("You busted!")
            exit()
        else:
            return player_score
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
        print("???")
        return False
