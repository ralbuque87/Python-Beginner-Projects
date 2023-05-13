import random

levels = ["easy", "medium", "hard"]
guesses = 0

# easy = range 10, 3 chances
# medium = range 50, 5 chances
# hard = range 100, 10 chances

while True:
    level = input(
        "welcome to the number guessing game, select level (easy/medium/hard): "
    )
    if level.lower() not in levels:
        print("Enter valid level")
        continue
    else:
        break

if level.lower() == "hard":
    range = 100
    max_guesses = 10
elif level.lower() == "medium":
    range = 50
    max_guesses = 5
else:
    range = 10
    max_guesses = 3

random_number = random.randint(0, range)
# print("random number is: ")
# print(random_number)

print("Guess a number between 0 and")
print(range)

while True:
    user_guess = input("")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number:")
        continue

    if user_guess > random_number and max_guesses != guesses:
        guesses += 1
        print("Guess lower: ")
        print("Guesses left: ")
        print(max_guesses - guesses)
        continue

    elif user_guess < random_number and max_guesses != guesses:
        guesses += 1
        print("Guess higher: ")
        print("Guesses left: ")
        print(max_guesses - guesses)
        continue

    elif max_guesses == guesses:
        print("you have reached max number of guesses, you lost!")
        break

    else:
        print("You got it! You Win ")
        break


print("Thanks for playing! Amount of guesses: ")
print(guesses)
