import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(
            input(f"Guess a number between 1 and {x} ->  "))
        print(guess)
        if guess < random_number:
            print("Sorry ! Guess again too low")
        else:
            if guess == random_number:
                print("You got it")
                break
            print("Sorry guess again too high")


guess(2000)
