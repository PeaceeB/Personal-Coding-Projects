# In this game, the compouter has a secret number, and the user has to guess
#that secret number

#The computer has to generate a secret number for us to guess, and in order for
#us to do that, we have to import random. For example random.randint.
#This function returns intergers.

import random

def guess(x): #By making x a parameter, we can pass that into this random get number
#function.
    random_number = random.randint(1, x) #<-This will return a random number for us
    # to guess.
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too Low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")

# User Secret Number Game
def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low # could also be high b/c low = high
            feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1

        print(f"Yay! The computer guessed your number, {guess}, correctly!")


computer_guess(10)
