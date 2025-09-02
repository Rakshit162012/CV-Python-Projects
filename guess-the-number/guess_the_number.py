```python
import random

print("Guess the Number (1–100)")
number = random.randint(1, 100)

while True:
    try:
        guessed_number = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guessed_number == number:
        print("Congratulations! You guessed the number!")
        break
    elif guessed_number < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
