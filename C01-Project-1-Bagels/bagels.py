# If the program is run (instead of imported), run the game
import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
  print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {}-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

  # Main game loop
  while True:
      # This store the secret number the player needs to guess
      secretNum = getSecretNum()
      print('I have thought up a number.')
      print('Youhave {} guesses to get it.'.format(MAX_GUESSES))

      numGuesses = 1
      while numGuesses <= MAX_GUESSES:
          guess = ''
          # Keep looping until then enter a valid guess
          while len(guess) != NUM_DIGITS or not guess.isdecimal():
              print('Guess #{}: '.format(numGuesses))
              guess = input('> ')
          numGuesses += 1

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digit."""
    # Create a list of digits 0 to 9
    numbers = list('0123456789')
    # Shuffle them into random order. 
    random.shuffle(numbers)
    print(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNumber):
  '''Returns a string with the pico, fermi,  bagels clue for a guess
  and secret number pair.'''
  if guess == secretNum:
      return 'You got it!'

  clues = []

  for i in range(len(guess)):
      if guess[i] == secretNum[i]:
          # A correct digit is in the correct place
          clues.append('Fermi')
      elif guess[i] in secretNum:
          # A correct digit is in the incorrect place
          clues.append('Pico')
  if len(clues) == 0:
      # There are no correct digits at all
      return 'Bagels'
  else:
      # Sort the clues into alphabetical order so their original order
      # doesn't give information away.
      clues.sort()
      # Make a single string from the list of string clues. 
      return ' '.join(clues)
if __name__ == '__main__':
    main()
