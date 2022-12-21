import utils
import random
#players Inputs: Name, Inputs:Rock,Paper,Scissors

#player's Name
player_name = input('Please enter your name: ')

#player's Input: Rock, Paper Or Scissors
print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a digit(0-2): '))

#Calling the Print hand function making sure its validated using the validate function
if utils.validate(player_hand) == True:

    #Computer session
    computer_hand = random.randint(0,2)

    #Calling the player input with the print_hand function
    utils.print_hand(player_hand, player_name)

    #Calling the computer hand with the print_hand function
    utils.print_hand(computer_hand, 'Computer')

    #Using the Judge function to announce the winner
    result = utils.judge(player_hand, computer_hand);
    print('RESULT: ' + result)
else:
    print('How far na? I gave you a range of values (0-2). You want to spoil my Program abi?')