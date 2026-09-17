# Tic Tac Toe

A simple terminal-based implementation of the famous game **Tic Tac Toe**, written in Python.

This project is intended as a **beginner programming and logic-building exercise**. It demonstrates how a relatively small game can be built using variables, lists, functions, loops, conditions, and user input.

## About

The game is played on a 3 × 3 board:

```text
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
-----------
```

The game internally represents the board using a **1D list** containing 9 elements.

Each cell can have one of three states:

* `N` — Empty
* `X` — Player X
* `O` — Player O

The players take turns entering the index of the cell they want to mark.

The game ends when:

* X gets three cells in a row.
* O gets three cells in a row.
* All cells are filled without a winner, resulting in a draw.

## Running the Game

Make sure Python is installed, then run:

```bash
python main_proc_tui.py
```

Follow the instructions in the terminal to play.

## How Winner Detection Works

There are 8 possible ways to win:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

The program represents these winning combinations using indexes:

```text
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]

[0, 3, 6]
[1, 4, 7]
[2, 5, 8]

[0, 4, 8]
[2, 4, 6]
```

For every combination, the program checks whether all three cells contain the same non-empty symbol.

## Exercise: Convert It to OOP

The current implementation intentionally uses a **procedural programming** approach.

Your exercise is to implement the same game using **Object-Oriented Programming (OOP)**.

Create a new file:

```text
main_oop_tui.py
```

and recreate the same behavior using classes.

Try to apply concepts such as:

* Classes
* Objects
* Encapsulation
* Abstraction
* Methods
* Object state

The goal is **not** simply to make the code longer by using classes. Think about:

> What should the object represent, and what responsibilities should it have?

For example, you might decide that the game itself should be responsible for maintaining the board, turns, and game state.

Once you have completed your implementation, push it to the repository.

The OOP implementation may eventually be merged into the repository so that students can compare the two approaches.

## Further Exercises

Once the basic implementation is working, try improving it yourself.

### 1. Handle Invalid Input

Currently, entering something like:

```text
abc
```

or:

```text
2.5
```

will cause the program to crash.

Modify `get_input()` so that invalid input is handled gracefully.

### 2. Add Replay

After a game finishes, ask:

```text
Play again? (y/n)
```

If the player chooses `y`, reset the game and start again.

### 3. Improve the Board

Make the board more visually appealing using:

* ANSI escape sequences
* Colors
* Better spacing
* A cleaner TUI layout

### 4. Add a Computer Player

Allow one player to play against the computer.

Start with a simple random strategy:

```text
Computer chooses a random empty cell.
```

Then try making the computer smarter.

### 5. Implement Minimax

For an advanced challenge, implement the **Minimax algorithm** so that the computer can make optimal moves.

This turns the project from a simple game into an introduction to **game-playing algorithms and search**.

**Happy Programming!**

— Tejas
