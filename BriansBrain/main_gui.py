# ===============================================================================
# @File:   main_gui.py (BriansBrain)
# @Brief:  Implementation of the BriansBrain Cellular Automaton
# @Author: Tejas
# @Date:   2026-09-23 Wed 
# @Notice: This is how games will render 3D graphics even though the screen is 2D.
# ===============================================================================

import pygame


def main():

    # NOTE(Tejas): I come from a C background so I like to put main in my code.
    # I have PTSD!

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("BriansBrain Cellular Automaton")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0)) 

        # Here you would add your BriansBrain logic and rendering code

        pygame.display.flip() # NOTE(Tejas): read double buffering to understand this.
        clock.tick(60) # NOTE(Tejas): limiting fps to 60

    pygame.quit()

if __name__ == "__main__":
    main()