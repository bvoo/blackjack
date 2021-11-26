import json
import os

file = '.\\player.json'
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, file)
    

def load_json():
    """
    This function loads the json file.
    """
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def modify_json(money, bet):
    """
    This function modifies the json file.
    """
    money -= bet
    with open(file_path, 'w') as f:
        f.write('{\n    "money": ' + str(money) + '\n}')

        
def player_bet():
    """
    This function allows the player to place a bet.
    """
    data = load_json()
    money = data["money"]
    print(f'You have ${money}')
    while True:
        bet = int(input("How much would you like to bet? "))
        print('\n')
        if bet > money:
            print("You don't have enough money!\n")
        else:
            modify_json(money, bet)
            return bet


def player_win(bet):
    """
    This function allows the player to win.
    """
    data = load_json()
    money = data["money"]
    money += bet+bet+bet
    modify_json(money, bet)
    print(f'Won {bet}!')


def player_draw(bet):
    """
    This function allows the player to draw.
    """
    data = load_json()
    money = data["money"]
    money += bet+bet
    modify_json(money, bet)
    print('Money refunded.')


def player_loss(bet):
    """
    This function allows the player to lose.
    """
    print(f'Lost {bet}!')