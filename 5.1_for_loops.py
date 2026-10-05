"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of campaign names.
# 2. Process: I loop through each name and show its position and the length of the name.
# 3. Out: One line per item, with the item, its position, and the computed length.
# 4. I compute the number of characters in each name so the reader can compare how long
#    each campaign name is in the list.


# Your code below
list_names = ["John", "Fury", "Donald", "Trump"]

for position, name in enumerate(list_names, start=1):
    print(f"Position {position}: {name} has {len(name)} letters.")
