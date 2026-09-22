# 3D in 2D

A simple implementation of **3D rendering in Python**, written using Pygame.

## About

A computer screen is 2D, but games can still make things look 3D.

The basic idea is to take a point:

```text
(x, y, z)
```

and convert it into a point on the screen:

```text
(x, y)
```

This project implements a very simple version of that idea.

We create a 3D object using a list of points and then connect those points with lines.

The code is intentionally simple and is meant for learning, not performance.

## Installing Pygame

Make sure Python is installed.

Then install Pygame using:

```bash
pip install pygame
```

If that doesn't work, try:

```bash
python -m pip install pygame
```

You can check that Pygame was installed correctly with:

```bash
python -m pygame.examples.aliens
```

A small Pygame window should open.

## Running the Program

Once Pygame is installed, run:

```bash
python main.py
```

You should see a rotating 3D cube.

## Creating Your Own Model

The model is defined using two lists:

```python
points = [
    Point(...),
    Point(...),
    Point(...),
]
```

and:

```python
faces = [
    [0, 1, 2, 3],
]
```

`points` contains the points that make up the model.

`faces` tells us which points to connect together.

Try replacing the cube with your own model.

For example, try making:

* A pyramid
* A house
* A chair
* A car
* Anything else you can think of

You can also ask ChatGPT to generate a model using the same `points` and `faces`
format.  Just paste the existing `points` and `faces` list to ChatGPT and ask to
generate a model of whatever you like in the same format and paste that code
their.

## Suggested Exercise

* Change the cube size.
* Change the rotation speed.
* Change the line color.
* Render the individual points.
* Create your own 3D model.

The goal is to understand the basic idea of how a 3D object can be drawn on a 2D screen.

**Happy Programming!**

— Tejas
