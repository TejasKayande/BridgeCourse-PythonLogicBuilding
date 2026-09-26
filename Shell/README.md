# Shell

A simple command-line shell implemented in Python.

This project is mainly an exercise in understanding how command-line shells work and how programs can be launched and controlled from another program.

## Running

Run the shell with:

```bash
python main.py
```

You can then enter commands:

```text
$ help
$ pwd
$ dir
$ echo Hello World
$ gol
$ langtons_ant
$ tictaktoe
$ exit
```

## How Commands Work

Commands are represented using the `Command` class.

Each command contains:

```text
Name
Function
Minimum number of arguments
Maximum number of arguments
... and more things to come
```

For example:

```python
Command("echo", echo, 1, None)
```

This means that the `echo` command calls the `echo()` function and accepts at least one argument.

New commands can be added by creating a function and registering it in `register_commands()`.

## Exercises

- [ ] There are several TODOs in the code for extending the shell.
- [ ] You are always welcome to add your own commands.

The goal is to gradually turn this simple command dispatcher into a more complete shell while learning how command-line programs work.


**Happy Programming!**

— Tejas