# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This function asks the user for their name and prints it to the screen
import random

# Assignment 2
def grab_name():
    # Prompts user to enter their name
    name = input("What is your name?")
    # Print user's name
    print(f'Nice to meet you, {name}!')
    # Asks the user for a number
    number = float(input("Please respond with a number:"))
    # Multiplies the number by itself and printers result
    print(number * number)
    # Ask the user for a word
    countphrase = input("Please enter a word:")
    # Prints the length of the string
    print(len(countphrase))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Assignment 3
# This function uses a two-dimensional array and loops to create text art
def w4loops():
    # Creates the array
    art = [['.', '*', 'o', '.', '*', 'o'],
        ['.', 'o', 'o', '*', '.', '*'],
        ['o', 'o', '*', '*', '*', '.'],
        ['.', '*', 'o', '.', '*', 'o'],
        ['o', 'o', '*', '*', 'o', '.'],
        ['.', 'o', 'o', '*', '*', 'o'],
        ['*', 'o', 'o', 'o', '*', '.'],
        ['*', 'o', 'o', 'o', '*', 'o'],
        ['*', '*', '.', 'o', 'o', '*']]
    # Loops print
    for star in art:
        for x in star:
            print(x, end=' ')
        print()

# This function simulates a coin flip
def w4coin_flip():
    # Welcomes user and prompts them to enter a number corresponding to heads or tails
    user_choice = int(input('Welcome to CoinFlip! Please enter 0 or 1.'))
    # Uses an RNG to randomly generate a 1 or 0
    pc_random = random.randint(0, 1)
    # Determines winner
    if user_choice == 1 and pc_random == 1:
        print(f"I got {pc_random} and you chose {user_choice}")
        print('I win!')
    else:
        print(f"I got {pc_random} and you chose {user_choice}")
        print('You win!')

# Main caller
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Zack')
    grab_name()
    w4loops()
    w4coin_flip()