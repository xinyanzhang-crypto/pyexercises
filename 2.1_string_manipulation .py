"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence entered by the user.
# 2. Process: I clean the text, change its case, and replace spaces with a separator.
# 3. Out: Four different versions of the same sentence.
# 4. My four transformations are: strip() to remove extra spaces, lower() to standardize
#    text for matching, title() to make it look tidy in a heading, and replace(" ", " - ")
#    to make words easier to separate in a report.


# Your code below
sentence = input("Enter a sentence: ")

cleaned = sentence.strip()
lower_case = cleaned.lower()
title_case = cleaned.title()
with_dash = cleaned.replace(" ", " - ")

print("Original:", sentence)
print("Cleaned:", cleaned)
print("Lowercase:", lower_case)
print("Title case:", title_case)
print("With dashes:", with_dash)
