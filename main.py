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

# Assignment 4

# Computer = X
# User = O

grid = [[1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]]
free_spaces = []

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+""")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user_choice = int(input("Enter your move: "))
            for i in range(len(free_spaces)):
                if user_choice == board[free_spaces[i][0]][free_spaces[i][1]]:
                    board[free_spaces[i][0]][free_spaces[i][1]] = 'O'
                    return
        # Makes an exception for an error so the function can work as intended.
        except ValueError:
            continue


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    for x in range(0, 3):
        for y in range(0, 3):
            if str(board[x][y]) != 'O' and str(board[x][y]) != 'X':
                free_spaces.append(tuple((x, y)))


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if sign == 'X':
        player = "AI"
    else:
        player = "User"

    # Checks for wins by column
    count = 0
    for x in range(0, 3):
        if count == 3:
            break
        else:
            count = 0
        for y in range(0, 3):
            if board[x][y] == sign:
                count += 1

    # Checks for wins by row
    if count != 3:
        for x in range(0, 3):
            if count == 3:
                break
            else:
                count = 0
            for y in range(0, 3):
                if board[y][x] == sign:
                    count += 1

    # Checks for diagonal wins
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        count = 3
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        count = 3
    if count == 3:
        print(f"The winner is: {player}!")
        exit()
    else:
        tie = 0
        for x in range(0, 3):
            for y in range(0, 3):
                if board[x][y] == 'X' or board[x][y] == 'O':
                    tie += 1

        if tie == 9:
            print("The game is a tie!")
            exit()

def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        ai_rand = random.randrange(1, 10)
        for j in range(len(free_spaces)):
            if ai_rand == board[free_spaces[j][0]][free_spaces[j][1]]:
                board[free_spaces[j][0]][free_spaces[j][1]] = 'X'
                return

# Main caller
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Zack')
    # grab_name()
    # w4loops()
    # w4coin_flip()

    display_board(grid)
    while True:
        make_list_of_free_fields(grid)
        enter_move(grid)
        display_board(grid)
        victory_for(grid, 'O')
        make_list_of_free_fields(grid)
        draw_move(grid)
        display_board(grid)
        victory_for(grid, 'X')
