import random

answer = random.randint(1, 300)
guess = 0
try:
    while guess != answer:
        guess = int(input("Pick a number between 1-300 or -1 to exit"))
        if guess == -1:
            print("Thanks for playing!")
            break
        if guess > answer:
            print("Your number is too high try again")
        elif guess < answer:
            print("Your number is too low try again")
        else:
            print("Correct! The random number was ", answer)
            break

except ValueError:
    print("Value Error occured")
except BaseException:
    print("Error occured at the BaseException")