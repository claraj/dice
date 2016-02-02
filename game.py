import time
import threading
import random
from colorama import init, Fore, Back, Style
#https://pypi.python.org/pypi/colorama


# In this game, the user and computer compete to roll one die each, as fast as they can
# The most points rolled (the number shown on the die) after 10 seconds is the winner
# Computer is throttled so can only roll once every 1.5 seconds
# User rolls by typing "roll" into the terminal


timeup = False

human_score = 0
computer_score = 0

space = '                                    '
#A hacky way of displaying computer output on the right of the screen

def main():

    init(autoreset=True)  #Initalize colorama, for printing colors at terminal
    print('Try to roll the dice as many times as you can after...')

    countdown(3, 'go!')

    #Start a timer which will call the end_game method after 10 seconds
    game_length = 10
    game = threading.Timer(game_length, end_game)
    game.start()

    #Create and start computer playing thread
    #Create and start human playing thread
    computer = threading.Thread(name="computer", target=computer_play)
    human = threading.Thread(name="human", target=human_play)
    computer.start()
    human.start()


def end_game():

    #Kill threads by setting global timeup to be true.
    #Human and computer threads check this value and use it to determine when to exit
    global timeup
    timeup = True

    print()
    print (Back.BLUE + '***  Computer Score: {} ***'.format(computer_score))
    print (Back.BLUE + '***    Human score: {}  ***'.format(human_score))

    if (human_score > computer_score):
        print("Human wins")
    elif (human_score < computer_score):
        print("Computer wins")
    else:
        print("A tie")

    #TODO Waits for user input afte game is over. Can you see why?
    #Suggestions for fixes?


def computer_play():

    global computer_score
    computer_score = 0

    while not timeup:
        dice = rolldice()
        print(Fore.GREEN + space + "I rolled a {}".format(dice))
        computer_score += dice
        print(Fore.GREEN + space + "My total score is {}".format(computer_score))
        time.sleep(1.5)


def human_play():

    global human_score
    human_score = 0

    user_input = "ROLL"
    while not timeup:
        roll = input(Fore.BLUE + "Type " + user_input + " to roll!")
        if roll == user_input:
            dice = rolldice()
            print(Fore.MAGENTA + 'You rolled a {}'.format(dice))
            human_score += dice
            print(Fore.MAGENTA + 'Your total score is {}'.format(human_score))
        if roll != user_input and not timeup :
            print(roll + " " + user_input + " " + str(timeup))
            print(Fore.BLUE + 'Try typing {} !!'.format(user_input))




def rolldice():
    return random.randint(1,6)


def countdown(startfrom, message):
    for n in range(startfrom):
        print(str(startfrom - n) + " ...")
        time.sleep(1)

    print(message)


if __name__ == "__main__":
    main()
