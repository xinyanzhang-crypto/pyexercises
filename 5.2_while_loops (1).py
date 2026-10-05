"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A user response to "Do you want to continue? (yes/no)".
# 2. Process: I strip spaces, convert to lowercase, count each attempt, accept
#    "Yes", "yes" and " yes " as the same answer, and stop when the user says "no".
# 3. Out: A short summary showing how many attempts were used and the final outcome.
# 4. My stop condition is the answer "no". My maximum number of attempts is 5.
#    My summary contains the number of attempts used and the last valid answer.


# Your code below
attempts = 0

while attempts < 5:
    attempts += 1
    choice = input(f"Attempt {attempts}/5 - Do you want to continue? (yes/no): ").strip().lower()

    if choice == "no":
        print("Stop condition reached: you said no.")
        print(f"Summary: used {attempts} attempt(s). Final answer: {choice}.")
        break

    if choice == "yes":
        print("You said yes, so the loop continues.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

    if attempts == 5:
        print("Maximum attempts reached. Stopping the loop.")
        print(f"Summary: used {attempts} attempt(s). Final answer: {choice}.")
        break
