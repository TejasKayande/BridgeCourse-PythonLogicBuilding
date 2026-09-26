# ===============================================================================
# @File:   main.py (Shell)
# @Brief:  Implementing a command line shell
# @Author: Tejas
# @Date:   2026-09-26 Sat
# ===============================================================================

# NOTE(Tejas): Their are certain commands that we cant write code for because we
# dont have access to it, like clearing the console window which is controled by
# the program that is rendering the console window. we have to ask that program
# from our program to perform that command. for that we need to use this module.
import os

# NOTE(Tejas): Following are all the commands that our shell supports.
# You can create your own commands but creating a function and adding it to the
# list in register_commands function below. Make sure the function signature is
# same as the other commands. def command_name(shell_context, args): 

# NOTE(Tejas): This is one thing I like about python, even though these
# functions dont know what shell_context is right now, they still run fine
# because they are called only after we define what shell_context is.
def exit(shell_context, args):
    print("Exiting the shell...")
    shell_context.running = False

def help(shell_context, args):
    print(shell_context.help_str)

def echo(shell_context, args):
    print('"', end="")
    print(" ".join(args), end="")
    print('"')

def clear(shell_context, args):
    # NOTE(Tejas): This is a hacky way to clear the console window. It works on
    # Windows and Linux but not on MacOS. Note that system is deprecated, but
    # this works for us for now.
    os.system('cls' if os.name == 'nt' else 'clear')


# NOTE(Tejas): This is a very interesting pattern I learned while implementing
# the UCI for a Chess application. you have a bunch of commands that you
# implement using a function so a function is a command, it has a name and it is
# of type Command (conceptually). Then you just match the users input to the
# list of commands you have and if matched you just call the
# proc(procedure/function) associated with that command name.
class Command:
    def __init__(self, name, proc, min_no_of_args, max_no_of_args):
        self.name = name
        self.proc = proc
        self.min_no_of_args = min_no_of_args
        self.max_no_of_args = max_no_of_args

def register_command():
    commands = [
        Command("exit" , exit , 0, 0),
        Command("help" , help , 0, 0),
        Command("echo" , echo , 1, None), # NOTE(Tejas): None means no limit.
        Command("clear", clear, 0, 0),
    ]

    return commands

def build_help_string(commands):
    # TODO(Tejas): Make the help menu actually explain what each command does.
    help_str = "Available commands:\n"
    for cmd in commands:
        help_str += f"  {cmd.name} (expects between {cmd.min_no_of_args} and {cmd.max_no_of_args} arguments)\n"
    return help_str


# NOTE(Tejas): Lets use a bit of OOP of this just to see if we like it or not!
# Althogh think of this as a C struct and not a class. Its just Encapsulation
class ShellContext:
    def __init__(self):
        self.commands = []
        self.running = False
        self.help_str = ""

def main():

    shell_context = ShellContext()
    shell_context.commands = register_command()
    shell_context.help_str = build_help_string(shell_context.commands)
    shell_context.running = True

    while shell_context.running:
        print("> ", end="")

        # TODO(Tejas): we dont want to use input() because it is line oriented
        # and we cant process inputs like ctrl or the arrow keys.
        c = input().split(" ")

        command   = c[0]
        arguments = c[1:]

        # TODO(Tejas): Add better error messages.

        cmd_found = False
        for cmd in shell_context.commands:
            if cmd.name == command:

                arg_count = len(arguments)
            
                if arg_count < cmd.min_no_of_args:
                    print(
                        f"Error: {command} expects at least "
                        f"{cmd.min_no_of_args} arguments."
                    )

                elif cmd.max_no_of_args is not None and arg_count > cmd.max_no_of_args:
                    print(
                        f"Error: {command} expects at most "
                        f"{cmd.max_no_of_args} arguments."
                    )

                else:
                    cmd.proc(shell_context, arguments)
                    cmd_found = True

        if not cmd_found:
            print(f"Error: Command '{command}' not found.")

if __name__ == "__main__":
    main()