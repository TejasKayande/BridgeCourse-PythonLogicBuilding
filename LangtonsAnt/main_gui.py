# ===============================================================================
# @File:   main_gui.py (LagntonsAnt)
# @Brief:  Implementation of LangtonsAnt GUI
# @Author: Tejas
# @Date:   2026-09-26 Sat
# @Notice: 
# @Source: https://en.wikipedia.org/wiki/Langton%27s_ant
# ===============================================================================

# NOTE(Tejas): This program is same as the TUI version just we change the
# print_state to render_state and use pygame

# IMPORTANT(Tejas): Before you read the code I want you to go through the wiki article
# and understand what we are trying to build!!!

# NOTE(Tejas): The way we program this is quite similar to GameOfLife, so look
# at that code first and then come back here. I will try to explain the
# differences here.

WIDTH = 50 * 2
HEIGHT = 40 * 2
CELL_SIZE = 20 // 2

import pygame
G_screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
pygame.display.set_caption("Langton's Ant")
G_clock = pygame.time.Clock()

# NOTE(Tejas): This is state of each cell, we can either have a cell to be white
# or black (You can rename these to BLACK and WHITE if you want).
STATE_UNSET = 0
STATE_SET   = 1

# NOTE(Tejas): helpers so we know which direction the ant is facing.
# I have arraged them in a clockwise manner because of a reason!
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

# NOTE(Tejas): you could use any datatype to represent the position on the ant
# like a tuple, a list, a dict with x and y keys, but we are representing the row
# and column of the ant.
g_ant_x = 0
g_ant_y = 0
g_ant_facing = 0

g_grid = []

def init():

    global g_ant_x, g_ant_y, g_ant_facing
    global g_grid

    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append(STATE_UNSET)
        g_grid.append(row)

    g_ant_x = WIDTH // 2
    g_ant_y = HEIGHT // 2
    g_ant_facing = UP

def turn_and_move_ant_right():

    global g_ant_facing, g_ant_x, g_ant_y

    new_ant_x = g_ant_x
    new_ant_y = g_ant_y

    # NOTE(Tejas): theres a cleaver way to do this using modulo operator which I
    # have commented out below. See if you can figure out how it works.
    # This is one of the very important properties of the modulo operator that I
    # use constantly in my code.

    # g_ant_facing = (g_ant_facing + 1) % 4

    if g_ant_facing == UP:
        g_ant_facing = RIGHT
        new_ant_x += 1
    elif g_ant_facing == RIGHT:
        g_ant_facing = DOWN
        new_ant_y += 1
    elif g_ant_facing == DOWN:
        g_ant_facing = LEFT
        new_ant_x -= 1
    elif g_ant_facing == LEFT: 
        g_ant_facing = UP
        new_ant_y -= 1

    if new_ant_x >= WIDTH:
        new_ant_x = 0
    if new_ant_x < 0:
        new_ant_x = WIDTH - 1
    if new_ant_y >= HEIGHT:
        new_ant_y = 0
    if new_ant_y < 0:
        new_ant_y = HEIGHT - 1

    g_ant_x = new_ant_x
    g_ant_y = new_ant_y

def turn_and_move_ant_left():

    global g_ant_facing, g_ant_x, g_ant_y

    new_ant_x = g_ant_x
    new_ant_y = g_ant_y

    # NOTE(Tejas): theres a cleaver way to do this using modulo operator which I
    # have commented out below. See if you can figure out how it works.
    # This is one of the very important properties of the modulo operator that I
    # use constantly in my code.

    # g_ant_facing = (g_ant_facing - 1) % 4

    if g_ant_facing == UP:
        g_ant_facing = LEFT 
        new_ant_x -= 1
    elif g_ant_facing == RIGHT:
        g_ant_facing = UP
        new_ant_y -= 1
    elif g_ant_facing == DOWN:
        g_ant_facing = RIGHT
        new_ant_x += 1
    elif g_ant_facing == LEFT: 
        g_ant_facing = DOWN
        new_ant_y += 1

    if new_ant_x >= WIDTH:
        new_ant_x = 0
    if new_ant_x < 0:
        new_ant_x = WIDTH - 1
    if new_ant_y >= HEIGHT:
        new_ant_y = 0
    if new_ant_y < 0:
        new_ant_y = HEIGHT - 1

    g_ant_x = new_ant_x
    g_ant_y = new_ant_y

def update_ant():

    # NOTE(Tejas): Rules:
    # 1. If the Ant is on a set square it unsets that square and turns left
    # 2. If the Ant is on an unset square it sets that square and turns right

    current_cell = g_grid[g_ant_y][g_ant_x]

    if current_cell == STATE_UNSET:
        g_grid[g_ant_y][g_ant_x] = STATE_SET
        turn_and_move_ant_right()

    else:
        g_grid[g_ant_y][g_ant_x] = STATE_UNSET
        turn_and_move_ant_left()

def render_state():

    G_screen.fill((0, 0, 0)) 

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if g_grid[i][j] == STATE_SET:
                pygame.draw.rect(
                    G_screen, (255, 255, 255), 
                    (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

    # NOTE(Tejas): Draw the ant as a red square
    pygame.draw.rect(
        G_screen, (255, 0, 0), 
        (g_ant_x * CELL_SIZE, g_ant_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )

    pygame.display.flip()

if __name__ == "__main__":
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        update_ant()
        render_state()

# TODO(Tejas): Can you do the following:

# 1. I am generally a follower of the DRY principle (Dont Repeat Yourself)
#    and I dont like how I have repeating code in both the turn functions
#    Can you refactor the code to remove the repetition?

# 2. Also I think a fuction in this code should do only one thing as its
#    very easy to debug if something goes wrong.
#    Can you refactor the turn functions into seperate functions that all do
#    one thing that they promise!

# 3. Think if you can add your own rules to how the ant moves and maybe we
#    can call this simulation <yourname>'s Ant!