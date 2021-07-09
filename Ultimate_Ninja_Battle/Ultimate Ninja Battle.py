"""
CP1401 2020-1 Assignment 2
Program 1 - Ninja Battle Game!!!
Student Name: Nikunj Bhatt
Date started: 25/05/2020

"""

import random

current_balance = 100
total_rounds = []


def main():
    print("Welcome to Ultimate Ninja Battle Combat!!! ")
    # ask for user name
    user_name = input("Please enter your name: ")
    print("Welcome,", user_name, "\n")
    display_menu()

    # ask for choice menu
    user_menu_input = input("").upper()
    continue_input = True

    # Validation for choice menu
    while continue_input:

        if user_menu_input == 'I':
            # display instructions to play the game
            display_instruction_menu()
            user_menu_input = input("").upper()

        elif user_menu_input == 'P':
            # play game
            play_game(user_name)

            if current_balance <= 0:
                # show balance history
                display_menu()
                user_menu_input = input("").upper()
                display_history(user_name)
                continue_input = False
            else:
                display_menu()
                user_menu_input = input("").upper()

        elif user_menu_input == 'Q':
            # quit the game
            display_history(user_name)
            continue_input = False
        else:
            # invalid choice of menu
            print("Invalid Choice", "\n")
            display_menu()
            user_menu_input = input("").upper()


def display_menu():
    # function for game menu
    print("\nYour current balance is ${:}".format(current_balance), '\n')
    print("Please choose from the following menu:")
    print("(I)nstructions")
    print("(P)lay game")
    print("(Q)uit game")


def display_instruction_menu():
    # function for welcome message
    print("\nWelcome to Ultimate Ninja Battle Combat!!! You will be fighting against the computer, and the winner gets "
          "bragging rights. For each turn you will be asked to use one of the 6 attacks below:")
    display_sub_menu()
    print("Choose wisely.\n")
    display_menu()


def display_sub_menu():
    # function for types of attacks
    print("(1) Punch of Fury ")
    print("(2) Kick of Punishment ")
    print("(3) Sword of Justice ")
    print("(4) Shuriken of Vengeance")
    print("(5) Nunchucks of Anger ")
    print("(6) Knife of Freedom ")


def play_game(user_name):
    # function for user's game moves.
    game_moves = ["Punch of Fury", "Kick of Punishment", "Sword of Justice", "Shuriken of Vengeance", "Nunchucks of "
                                                                                                      "Anger",
                  "Knife of Freedom"]
    global current_balance

    # get random computer's move
    computer_move = random.randint(1, 6)

    # ask for user input for bet amount
    print("\nPlease enter the amount to bet. All bets must be multiples of 5.")
    bet_amount = int(input("You choose to bet $"))

    # Validation for bet amount
    while (bet_amount % 5 != 0) or (bet_amount > current_balance):
        print("\nThat is not a valid amount. Your bet must be a multiple of 5, and be within your means.")
        print("Please enter the amount to bet. All bets must be multiples of 5.")
        bet_amount = int(input("You choose to bet $"))

    print("\n", user_name, ",you must choose one of the following attacks: ")

    display_sub_menu()

    # ask for user input for attack
    game_input = int(input(""))

    # Validation for selected attack by user
    while game_input not in range(1, 7):
        print("invalid choice", "\n")
        print(user_name, ",you must choose one of the following attacks: ")
        display_sub_menu()
        game_input = int(input(""))

    print(user_name, ",you chose:", game_moves[game_input - 1])
    print("The computer chose: ", game_moves[computer_move - 1])

    # Assigning game result matrix in list
    game_list = [["Tie No Winner", "Player Wins", "Player Wins", "Player Loses", "Player Loses", "Player Wins"],
                 ["Player Loses", "Tie No Winner", "Player Wins", "Player Wins", "Player Loses", "Player Wins"],
                 ["Player Loses", "Player Loses", "Tie No Winner", "Player Wins", "Player Wins", "Player Loses"],
                 ["Player Wins", "Player Loses", "Player Loses", "Tie No Winner", "Player Wins", "Player Loses"],
                 ["Player Wins", "Player Wins", "Player Loses", "Player Loses", "Tie No Winner", "Player Wins"],
                 ["Player Loses", "Player Loses", "Player Wins", "Player Wins", "Player Loses", "Tie No Winner"]]

    game_result = game_list[computer_move - 1][game_input - 1]

    # process game result
    if game_result == 'Player Wins':
        current_balance = current_balance + bet_amount
        print("\nCongratulations, you won ", user_name)

    elif game_result == 'Tie No Winner':
        print("\n", user_name, ", It's a Tie!")

    else:
        current_balance = current_balance - bet_amount
        print("\nUnfortunately,", user_name, ",you lost")

    global total_rounds  # list storing the balance for all rounds
    total_rounds.append(current_balance)


def display_history(user_name):
    # display game history of user
    print("\nGoodbye", user_name, ".Your final balance is: ${:}".format(current_balance))
    print("Your balance history is:")
    print("Starting balance: $100")
    global total_rounds
    size = len(total_rounds)

    for i in range(size):
        print("After round {}: ${}".format(i + 1, total_rounds[i]))


main()
