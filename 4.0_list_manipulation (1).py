"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of monthly marketing channel budgets in euros.
# 2. Process: I store the values, print the full list, choose one item, sort them,
#    and calculate the total monthly budget.
# 3. Out: The whole list, one selected channel budget, the sorted list, and the total.
# 4. My list is about marketing channel spending. I computed the total budget to see
#    how much the team spent across all channels in one month.


# Your code below
marketing_budget = [1200, 1500, 900, 2000, 1100, 1750, 800, 1300]

print("Full list:", marketing_budget)

selected_channel = marketing_budget[3]
print("Selected budget:", selected_channel)

sorted_budget = sorted(marketing_budget)
print("Sorted list:", sorted_budget)

total_budget = sum(marketing_budget)
print("Total monthly budget:", total_budget)
