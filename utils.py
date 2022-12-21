#Validating the users Input
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

#Judging the winner
def judge(player,computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'You lose, Computer wins'
    elif player == 1 and computer == 2:
        return 'You lose, Computer wins'
    elif player == 2 and computer == 1:
        return 'You lose, Computer wins'
    else:
        return 'You win, bravo/brava'

#Handling Inputs
def print_hand( hand,name = 'Guest',):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + " picked: " + hands[hand])