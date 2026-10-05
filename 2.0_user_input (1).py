"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's name and age.
# 2. Process: I read both values, convert the age to an integer, and combine them in a sentence.
# 3. Out: A sentence showing the name and age together.
# 4. My two fields are the customer's name and age, which I would use in a registration form
#    to identify the customer and segment them by age group.


# Your code below

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name is:", name)
print("Age is:", age)

print("Your name is " + name + " and your age is " + str(age) + ".")

