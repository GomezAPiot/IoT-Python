import random
import collections

lenght = 4
guesses = 12
pattern = [random.choice('abcdef') for _ in range(lenght)]
print('Guess the 4 right letters from a to f')
counted = collections.Counter(pattern)


def running():
    guess = input('\n?: ')
    guess_count = collections.Counter(guess)
    close = sum(min(counted[k], guess_count[k]) for k in counted)
    exact = sum(a == b for a, b in zip(pattern, guess))
    close -= exact
    print('exact: {}. close: {}.'.format(exact, close))
    return exact != lenght


for attempt in range(12):
    if not running():
        print('Congrats, You guessed right!')
        break

    else:
        print('\nGuesses remaining', guesses - 1 - attempt)

else:
    print('\nGame over. The code was {}.'.format(''.join(pattern)))
