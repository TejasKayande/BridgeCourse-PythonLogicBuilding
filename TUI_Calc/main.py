# ===============================================================================
# @File:   main.py (TUI_Calc)
# @Brief:  Implementation of a HomeWork given on date <2026-09-15 Tue>
# @Author: Tejas
# @Date:   2026-09-15 Tue
# @Notice: This was created to demonstrate how I would write the code for the
#          given homeword question.
# ===============================================================================

# NOTE(Tejas): Functions used that maybe unfamilier:
#
# 1. str.center() -> when used with print, str.center can leave a gap of specified
#                    size on either side of the string so that it fits centered
#                    inside a given width (in the param list).
#    used on line numbers: 50
#
# 2. str.lower() -> turns all the char of the string to lower char, ex: A becomes a.
#                   this comes in handy when we compare and dont have to worry
#                   about comparing both lower and upper case variations
#    used on line numbers: 57
#
# 3. str.split() -> this function identifies words seperated by spaces (' ') in
#                   a string and adds them to a list of words.
#                   ex: "this is a string".split() -> ['this', 'is', 'a', 'string']
#    used on line numbers: 65, 77, 98, 124

# TODO(Tejas): For everyone!
# whenever you learn about exception handling I want you to go ahead and handle errors
# casting errors, zerodivied errors. Push it to this repo and if your code is okay
# I will merge it in this repo

WIDTH = 30
TITLE = "CALCULATOR"
MENU = """
1. Addition (+)
2. Subtraction (-)
3. Multiplication (x)
4. Division (/)
5. Average
6. Factorial (!)
7. exit / quit
"""

if __name__ == "__main__":

    while True:

        # NOTE(Tejas): This is just for aesthetic purposes you can just do
        # print(TITLE) and that serves the purpose.
        print(''.center(WIDTH, '_'))
        print(TITLE.center(WIDTH, '-'))

        print(MENU, end="")
        print(''.center(WIDTH, '_'))

        choice = input("Enter a choice: ")
        choice = choice.lower()

        match choice:
            case '1' | "add" | "addition" | '+':
                print("Addition: ")
                print("Please enter all the numbers you want to add separated by a space (' ')")
                print("Hit Enter when you are done all the entering numbers!")

                numbers = input("Space Separated Numbers > ").split()
                total = 0
                for n in numbers:
                    total += float(n)
                print("Performing Addition...")
                print("Result: ", total)

            case '2' | "sub" | "subtraction" | '-':
                print("Subtraction: ")
                print("Please enter all the numbers you want to subtract separated by a space (' ')")
                print("Hit Enter when you are done entering all the numbers!")

                numbers = input("Space Separated Numbers > ").split()

                if numbers:
                    total = float(numbers[0])
                else:
                    total = 0

                # NOTE(Tejas): This is string slicing [start_index : stop_index : step_size]
                #              we basically want to skip the first element here
                #              as we have already assigned it to total above
                for n in numbers[1:]: 
                    total -= float(n)

                print("Performing Subtraction...")
                print("Result: ", total)

            case '3' | "multi" | "multiplication" | 'x':
                print("Multiplication: ")
                print("Please enter all the numbers you want to subtract separated by a space (' ')")
                print("Hit Enter when you are done entering all the numbers!")

                numbers = input("Space Separated Numbers > ").split()
                total = 1
                for n in numbers:
                    total *= float(n)

                print("Performing Multiplication...")
                print("Result: ", total)

            case '4' | "div" | "division" | '/':
                # NOTE(Tejas): for division I decided to only allow 1 numerator over 1 denominator
                #              to avoid having to perform arithmetic ops on all the numbers provided
                #              in the numerator and denominator. But you can certainly try it and handle
                #              cases like: (2 + 3 - 4) / (9 - 2 + 1)
                num  = float(input("Enter the numerator> "))
                deno = float(input("Enter the denominator> "))
                if deno != 0:
                    print("Performing Division...")
                    print("Result: ", num / deno)
                else:
                    print("Denominator cant be zero")

            case '5' | "avg" | "average":
                print("Average: ")
                print("Please enter the list that you want to find the average of by seperating each number by a space(' ')")
                print("Hit Enter when you are done entering all the numbers!")

                numbers = input("Space Separated Numbers > ").split()
                total = 0.0
                for n in numbers:
                    total += float(n)

                print("Calculating Average...")
                print("Result: ", total / len(numbers))

            case '6' | "fact" | "factorial" | '!':
                num = int(input("Enter a number: "))

                if num == 0:
                    print("Factorials can not be calculated for negative numbers!")
                else:
                    fact = 1
                    i = 1
                    while i <= num:
                        fact *= i
                        i += 1

                        print("Calculating Factorial...")
                        print("Result: ", fact)

            case '7' | 'exit' | 'quit':
                print("Exiting...")
                break

            case _:
                print("Unknown Command!")

