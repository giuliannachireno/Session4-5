

from random import randint

lives = 3
while lives > 0:
        diceroll = randint(1,6)
        if diceroll == 6:
            print("Congrats! You win!")
            break
        else:
            lives = lives - 1 #you lose a life
            print(f"You rolled a {diceroll}. You lose a life, lives left: {lives}")

else:
            print("You lose!")