print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
yesses = ["yes", "yep", "y"]
score = 0

if playing.lower() not in yesses:
    quit()

level = input("Okay! Let's play, what Level difficulty you want? (Easy/Hard)")

if level.lower() == "easy":
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

if level.lower() == "hard":
    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does PSU stand for? ")
    if answer.lower() == "power supply":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 2) * 100) + "%.")
