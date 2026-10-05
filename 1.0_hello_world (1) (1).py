"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: No special input; the program will print a message.
# 2. Process: I will print the same message five times, each with a number.
# 3. Out: Five numbered lines on the screen.
# 4. My message is "Good morning" because it is a simple greeting that is easy to read
#    and easy to count in the output.


# Your code below
for count in range(1, 6):
    print(f"{count}. Good morning")
