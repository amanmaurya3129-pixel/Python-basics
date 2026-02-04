Day 1 – Number Guessing Game

Objective:-

Create a simple interactive game where the computer generates a random number and the user tries to guess it.

Concepts Used:-

- "import random" → to generate unpredictable numbers
- "random.randint(1, 100)" → selects a number between 1 and 100
- "while True" loop → keeps game running until correct guess
- "if / elif / else" → compares user input with actual number
- "input()" → takes user input
- "int()" → converts string input to integer
- counter variable ("attempts") → tracks number of tries

Program Logic:-

1. Computer secretly picks a number.
2. User keeps guessing.
3. Program checks:
   - guess > number → Too High
   - guess < number → Too Low
   - guess == number → Win and stop loop
4. Display total attempts at the end.

What I Learned

- How loops control program flow
- Importance of condition checking
- How programs interact with users
- Basic debugging while handling inputs

Possible Improvements

- Add difficulty levels
- Limit attempts
- Handle invalid input (letters/symbols)

---

Learning outcome: Understood how logic + loops create an interactive program.