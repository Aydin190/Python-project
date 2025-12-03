import random

print("Dice Roller")

while True:
    roll = random.randint(1, 6)
    # print(roll)
    # Create a variable, name it guess. Take an input from the user that you guessed the number from 1 to 6.
    guess = int(input("Guess any number from 1-6"))
    # check if guess and roll is same. if it is similar, then print (your intuiton is great.) else print "wrong guess", dice short print roll.
    score = 0
    if guess == roll:
        print("Your intuition is great.")
        score+=1
    else:
        print(f"Unfortunately, that's the wrong guess. The dice showed {roll}")

    print(f"Your current score is {score}")

    again = input("Are you going to roll again?(y/n)")
    if again.lower() != 'y':
        print("Thanks for playing.")





        break

# Get an input from the user aksing for a number. If this number matches the random number the computer generated, then print "The intution is great for the user"
# Add a score counter, so create a score variable starting from 0, and when you guess it right, the score variable will increase by 1 point. And at the end, print the total score.
# Run this game exactly 10 rounds. At the end, print the final score out of 10. After that, create a if-else structure where if your score is 10, you have perfect intuituitrpn, >=7, great guessing skills, >= 4, not bad, keep trying else print better luck next time!.

