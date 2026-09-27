# Shooter

A simple top-down shooter game written in Python using **Pygame**.

This project is intended as a **beginner programming, OOP, and game-development exercise**. It demonstrates how a small game can be built using classes, objects, vectors, input handling, game loops, collision detection, and basic game physics.

## About

The game features a player that can move around the screen, aim using the mouse, and shoot bullets at enemies.

Enemies continuously move towards the player. The player loses health when an enemy reaches them.

The game ends when the player's health reaches zero.

The player can then press:

```text
R
```

to restart the game.

## Controls

| Input               | Action                  |
| ------------------- | ----------------------- |
| `W`                 | Move Up                 |
| `A`                 | Move Left               |
| `S`                 | Move Down               |
| `D`                 | Move Right              |
| `Left Mouse Button` | Shoot                   |
| `R`                 | Restart after Game Over |
| `ESC`               | Quit                    |

The player aims toward the current mouse position.

## Running the Game

Make sure Python and Pygame are installed.

Install Pygame with:

```bash
pip install pygame
```

Then run:

```bash
python main.py
```

## Game Loop

The game follows a simple three-stage structure:

```text
Input
  ↓
Update
  ↓
Render
```

## Exercises

The current implementation is intentionally simple. Try extending it yourself.

### 1. Add Accuracy and Score

Track:

* Number of bullets fired
* Number of enemies killed
* Accuracy

For example:

```text
Score: 25
Accuracy: 72%
```

### 2. Increase Difficulty

Make the game progressively harder.

You could increase:

* Enemy speed
* Enemy spawn rate
* Number of enemies
* Enemy health

Difficulty could increase based on time survived or score.

### 3. Improve Enemy Spawning

Currently enemies can spawn anywhere inside the screen.

Modify the spawning system so that enemies spawn **outside the visible play area** and move toward the player.

### 4. Add Different Enemy Types

Create different enemy classes or behaviors.

For example:

```text
Normal Enemy
Fast Enemy
Tank Enemy
```

Each type could have different:

* Speed
* Health
* Size
* Damage

### 5. Add a Camera

Allow the player to move beyond the boundaries of the screen.

Then implement a camera that follows the player.

This would turn the current fixed-screen game into a small scrolling world.

### 6. Improve the Game Over Screen

Add:

* Final score
* Enemies killed
* Accuracy
* Time survived

For example:

```text
Game Over

Score: 120
Enemies Killed: 24
Accuracy: 68%

Hit R to restart

```
The goal is not to build a production-quality game, but to understand how the different pieces of a game fit together.

**Happy Programming!**

— Tejas
