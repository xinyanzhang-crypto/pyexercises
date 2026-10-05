"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The original marketing budget list from exercise 4.0.
# 2. Process: I create four different orders of the same list and compare them to the
#    original to prove it is not damaged.
# 3. Out: The original list, a sorted copy, a reversed copy, and two in-place examples.
# 4. My four orders are: sorted(), reversed(), sort() on a copy, and reverse() on a copy.
#    sorted() and reversed() return new lists, while sort() and reverse() modify the list
#    in place.


# Your code below
original_budget = [1200, 1500, 900, 2000, 1100, 1750, 800, 1300]

print("Original list:", original_budget)
print("Sorted copy:", sorted(original_budget))
print("Reversed copy:", list(reversed(original_budget)))

copy_for_sort = original_budget.copy()
copy_for_sort.sort()
print("Sort on a copy:", copy_for_sort)

copy_for_reverse = original_budget.copy()
copy_for_reverse.reverse()
print("Reverse on a copy:", copy_for_reverse)

print("Original list at the end:", original_budget)
