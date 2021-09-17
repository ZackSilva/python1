# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This function asks the user for their name and prints it to the screen
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Zack')
    grab_name()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
