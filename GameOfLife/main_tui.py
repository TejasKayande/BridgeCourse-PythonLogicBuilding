# ===============================================================================
# @File:   main_tui.py (GameOfLife)
# @Brief:  Implementation of Conways Game of Life
# @Author: Tejas
# @Date:   2026-09-15 Tue
# @Notice: This is a simple implementation of conways game of life
# @Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# ===============================================================================

# IMPORTANT(Tejas): Before you read the code I want you to go through the wiki article 
# and understand what we are trying to build!!!

# NOTE(Tejas): we'll use basic random numbers to populate the initial state.
# You dont have to use this, you can populate it manually
import random
import time

WIDTH = 90
HEIGHT = 30

# NOTE(Tejas): this is my convention to put g_ before any global
# variables I use, you dont have to, but this is what I do...
g_grid = [] # This is a 2D array which we will populate in init()

ALIVE = 1
DEAD = 0

def print_state():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if g_grid[i][j] == ALIVE:
                print("O", end="")
            else:
                print(" ", end="")
        print()

def init():
    # NOTE(Tejas): I use the random module here to add random state to each cell (ALIVE or DEAD).
    # if you choose you can populate the grid
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            number = random.randint(0, 1)
            row.append(number)

        g_grid.append(row)


def count_neighbors(row, column):

    # NOTE(Tejas): put your thinking cap on and try to figure out what we are trying to do.
    # You have the game rules and also the name of the function is a big giveaway...

    count = 0

    for i in range(row - 1, row + 2):

        for j in range(column - 1, column + 2):

            # NOTE(Tejas): we want to skip the cell itself, we only want to count the neighbors
            if i == row and j == column:
                continue

            # NOTE(Tejas): we dont want to check outside the grid, so we skip those cells
            if i < 0 or i >= HEIGHT:
                continue
            if j < 0 or j >= WIDTH:
                continue

            if g_grid[i][j] == ALIVE:
                count += 1

    return count


def next_generation():

    # NOTE(Tejas): We have following rules to get the next generation of the grid.
    # The Rules of Game of Life:
    #   1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    #   2. Any live cell with two or three live neighbours lives on to the next generation.
    #   3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    #   4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    # Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

    new_grid = []

    for i in range(HEIGHT):
        row = []

        for j in range(WIDTH):
            neighbors = count_neighbors(i, j)

            if g_grid[i][j] == ALIVE:

                # NOTE(Tejas): Rule 1 & 3
                if neighbors < 2 or neighbors > 3:
                    row.append(DEAD)

                # NOTE(Tejas): Rule 2
                else:
                    row.append(ALIVE)

            else:

                # NOTE(Tejas): Rule 4
                if neighbors == 3:
                    row.append(ALIVE)
                else:
                    row.append(DEAD)

        new_grid.append(row)

    return new_grid

init()

# NOTE(Tejas): Every application has whats called a main loop or game loop.
# This will iterate for indefinitely, because we are working in a termainal
# the program will be terminated by hitting Ctrl+C or closing the terminal window.
# If this were a GUI application, we have a red cross in the top right corner
# to close a window.
while True:

    # NOTE(Tejas): Think of this as a way to clear the terminal for our redraw.
    print("\033[H", end="")

    print_state()

    # NOTE(Tejas): here we apply the rules to the current state of the grid.
    g_grid = next_generation()

    # NOTE(Tejas): Control simulation speed, adjust this value and see what happens...
    time.sleep(0.1)


# NOTE(Tejas): Once you think you understand the code
# Try modifying the program:
#  - [ ] Change the grid size.
#  - [ ] Change the simulation speed.
#  - [ ] Populate the grid manually instead of randomly.
#  - [ ] Experiment with different initial patterns.
#  - [ ] Try creating known Game of Life patterns such as a **glider**.
#  - [ ] Add a generation counter.
#  - [ ] Add support for pausing the simulation.
#  - [ ] Try implementing your own improvements.