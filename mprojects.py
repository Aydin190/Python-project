import random


print("Dice Roller")

score = 0

life = 3

maxRange = 6

for roundNumber in range(1, 11):
    # Check if life is 0, and print, you have 0 lives left. game over. give break statement.
    if life == 0:
        print("You have no lives left! Game Over.")
        break
    roll = random.randint(1, maxRange)
    guess = int(input("Guess any number from 1-6"))

    if guess == roll:
        print("Your intuition is great.")
        score+=1
        maxRange+=2

    else:
        print(f"Unfortunately, that's the wrong guess. The dice showed {roll}")
        life-=1

    print(f"Your current score is {score}")


print("Game Over")
print(f"Your final score is {score}/10")


# Create a if-else structure where if your score is 10, you have perfect intuituitrpn, >=7, great guessing skills, >= 4, not bad, keep trying else print better luck next time!.

if score == 10:
    print("You have perfect intuition! 🔥 ")
elif score >= 7:
    print("You have great guessing skills! 🧠 ")
elif score >= 4:
    print("Not bad. Keep trying! 🙂 ")
else:
    print("Better luck next time! 💀 ")







# Adding life systems from the heart mode to this game where you start with 3 lives and your wrong guess will lose 1 of ur lives, and the game ends when you lose all of your lives or you finish all the 10 rounds, the score still counts.

# Increase difficulty with each correct guess. Initially there are 1 to 6 rounds, after that it will be between dice 1-8.