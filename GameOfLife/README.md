# Conway's Game of Life

A simple terminal-based implementation of **Conway's Game of Life**, written in Python.

> **IMPORTANT:** Before reading the code, go through the [Wikipedia article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) and understand the rules of the game.

## About

Conway's Game of Life is a simple simulation of a grid of cells, where each cell can either be DEAD or ALIVE based on some rules

Reading the article is VERY IMPORTANT for you to understand this code.

PS
if reading is not your thing, watch this video
[Youtube Vide](https://www.youtube.com/watch?v=ouipbDkwHWA)

![Conways Game of Life](./docs/demo.gif)

## Rules

For each cell:

* A live cell with fewer than **2** live neighbors dies.
* A live cell with **2 or 3** live neighbors survives.
* A live cell with more than **3** live neighbors dies.
* A dead cell with exactly **3** live neighbors becomes alive.

## Running the Program

Make sure Python is installed, then run:

```bash
python main_tui.py
```

The simulation will continuously run in the terminal.

To stop it, press:

```text
Ctrl + C
```

I have named in main_tui.py becuase Im thinking of adding a gui version to this as well.

## Suggested Exercise

Don't just run the program. Try to understand how each part works.

In particular, try to figure out how `count_neighbors()` works **before** reading the implementation.

Then try modifying the program:

* Change the grid size.
* Change the simulation speed.
* Populate the grid manually instead of randomly.
* Experiment with different initial patterns.
* Try creating known Game of Life patterns such as a **glider**.
* Add a generation counter.
* Add support for pausing the simulation.
* Try implementing your own improvements.

**Happy Programming!**

— Tejas
