# this is a guess of game
import random
secretNumber = random.randint(1 , 20)
print('i am thinking of a number between 1 and 20.')

# ask the player to guess 5 times
for guessestaken in range(1,6):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break # this condition is correct guess!

if guess == secretNumber:
    print('good job! you guessed my number in' + 'str(guessestaken)' + 'guesses!')
else:
    print('nope you number i was thinking of was ' + str(secretNumber))
