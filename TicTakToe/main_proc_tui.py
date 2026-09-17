# ===============================================================================
# @File:   main.py (TicTakToe)
# @Brief:  Implementation of the famous game of Tic Tac Toe 
# @Author: Tejas
# @Date:   2026-09-17 Thu
# @Notice: 
# ===============================================================================

# TODO(Tejas): This a good example of a begineer project where you could implement 
# Object Oriented Principals like Encapsulation and Abstraction. For me I always
# prefer procedural programming if I can help it (which is often times the case for me).
# But the excercise for you is to convert this code to use OOP principles and
# see which implementation you like better.

# Create a file called main_oop_tui.py and implement OOP for this same behavior and push it
# if I like it I will merge it into this repo for others to see.

# NOTE(Tejas): This is what our game state would look like with their indexes:
#     1 | 2 | 3
#    -----------
#     4 | 5 | 6
#    -----------
#     7 | 8 | 9

# NOTE(Tejas): we use a 1D array to store the game state, now you could use a 2D
# array if you think it helps you visualise better, and change indexing accordingly
# like 1 becomes (0, 0) or (1, 1) depending on how you want to index it.
N = 0
X = 1
O = 2
g_game_state = []

g_turn = X # NOTE(Tejas): X always starts first, so we set the turn to X

# NOTE(Tejas): this is for our while loop, so we can value of this to False if
# we want to terminate the program
g_runing = True 

def reset_game_state():

    # NOTE(Tejas): This is one of the biggest problems with dynamically typed
    # and interpreted languages like Python: when I want to set the value of
    # g_game_state to a new value, Python does not understand if I want to
    # create a new variable called g_game_state or use the global variable,
    # so I have to explicitly tell Python that I want to use the global variable
    global g_game_state 
    global g_turn

    g_game_state = [
        N, N, N,
        N, N, N,
        N, N, N,
    ]

    g_turn = X

def get_input():

    if g_turn == X:
        print("X's turn")
    else:
        print("O's turn")

    # TODO(Tejas): Handle exception here if the user enters something that is not an integer.
    # The program will crash here if the user enters a string or a float, so we need to handle that.
    index = int(input("Enter the index of the cell you want to mark: "))
    if index < 1 or index > 9:
        print("Invalid index, please try again")
        return get_input()

    board_index = index - 1

    if g_game_state[board_index] != N:
        print("Cell already marked, please try again")
        return get_input()

    # NOTE(Tejas): 
    return board_index

def set_state(board_index, symbol):
    # NOTE(Tejas): since we are expecting our input to be correct, we are not
    # going to check it again here if the input is valid or the symbol is valid,
    # we are going to rely on the caller to not be an idiot

    # NOTE(Tejas): it is a good practice to Assert here that the input is valid
    # and the symbol is something related to the game.
    global g_turn
    g_game_state[board_index] = symbol

    # NOTE(Tejas): flip the turn, again you could use if else here. But I think
    # this looks better
    g_turn = O if g_turn == X else X 

def check_winner():

    # NOTE(Tejas): we are going to check all the possible winning combinations
    # and see if any of them have the same symbol, if they do then we have a winner
    # and we return the symbol of the winner, else we return N for no winner yet

    winning_combinations = [
        [0, 1, 2], # first row
        [3, 4, 5], # second row
        [6, 7, 8], # third row
        [0, 3, 6], # first column
        [1, 4, 7], # second column
        [2, 5, 8], # third column
        [0, 4, 8], # diagonal from top left to bottom right
        [2, 4, 6], # diagonal from top right to bottom left
    ]

    for combination in winning_combinations:
        if g_game_state[combination[0]] == g_game_state[combination[1]] == g_game_state[combination[2]] != N:
            return g_game_state[combination[0]]

    return N

def print_state():

    # NOTE(Tejas): here enumerate is a built-in function that returns both the
    # index and the value of the iterable if we just did for symbol in
    # game_state, we would not have the index of the symbol that we want to display 
    # for user convinence so that they know which index to enter to mark their symbol.

    for index, symbol in enumerate(g_game_state):
        if symbol == N:
            print(f" {index + 1} ", end="")
        elif symbol == X:
            print(" X ", end="")
        else:
            print(" O ", end="")

        if (index + 1) % 3 == 0:
            print()
            print("-----------")
        else:
            print("|", end="")

if __name__ == "__main__":

    reset_game_state()
    print_state()

    while g_runing:
        set_state(get_input(), g_turn)
        print_state()
        winner = check_winner()
        if winner == X:
            print("X wins!")
            g_runing = False
        elif winner == O:
            print("O wins!")
            g_runing = False

        if winner == N and N not in g_game_state:
            print("It's a draw!")
            g_runing = False

# TODO(Tejas): Can you implement the following features:
# 1. Allow the user to either exit or play again after a game is over
# 2. Add a engine that can play moves at random
# 3. Add a engine that can play the best move possible (hint: look into MiniMax algorithm)