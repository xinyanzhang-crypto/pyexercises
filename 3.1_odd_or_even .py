"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A number N entered by the user.
# 2. Process: I check each number from 1 to N and decide whether it is odd or even.
# 3. Out: One line per number, saying whether it is odd or even.
# 4. If the user enters 0, I show a message saying the number must be greater than 0.
#    If the user enters a negative number, I show a message saying only positive numbers are allowed.
#    If the user enters 5000 or more, I print a message saying the number is too large and stop.


# Your code below
n = int(input("Enter a positive number N: "))

if n <= 0:
    print("Please enter a number greater than 0.")
elif n >= 5000:
    print("This number is too large. Please enter a smaller number.")
else:
    for number in range(1, n + 1):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
