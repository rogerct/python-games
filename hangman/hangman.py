import random
import time
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 0   |
     |
     |
    ===''','''
 +---+
 0   |
 |   |
     |
    ===''','''
 +---+
 0   |
/|   |
     |
    ===''','''
 +---+
 0   |
/|   |
     |
    ===''','''
 +---+
 0   |
/|\  |
     |
    ===''','''
 +---+
 0   |
/|\  |
/    |
    ===''','''
 +---+
 0   |
/|\  |
/ \  |
    ===''']
# print(HANGMAN_PICS)
# print(HANGMAN_PICS[0])
words = 'soul mate rock guitar pain painfull javascript animal ruby moshpit'.split()

def get_random_word(word_list):
  # random string from the list
  word_index = random.randint(0, len(word_list) - 1)
  return word_list[word_index]

def display_board(missed_letters, correct_letters, secret_word):
  print(HANGMAN_PICS[len(missed_letters)])
  print()

  print('Missed Letters:', end=' ')
  for letter in missed_letters:
    print(letter, end='')
  print()

  blanks = '_' * len(secret_word)

  for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
      blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
      print(letter, end=' ')
    print()

def get_guess(already_guessed):
  while True:
    print('Guess a letter!')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
      print('Please enter a single letter.')
    elif guess in already_guessed:
      print('You have already guessed that better choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
      print('please enter a letter.')
    else:
      return guess

def playAgain():
  print('Do you want play again? yes or no')
  return input().lower().startswith('y')


print ('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
  display_board(missed_letters, correct_letters, secret_word)

  guess = get_guess(missed_letters + correct_letters)

  if guess in secret_word:
    correct_letters = correct_letters + guess

    found_all_letters = True
    for i in range(len(secret_word)):
      if secret_word[i] not in correct_letters:
        found_all_letters = False
        break
    if found_all_letters:
      print('Yes the secret word is "'+ secret_word + '"! You win!')
      game_is_done = True
  else:
      missed_letters = missed_letters + guess

      if len(missed_letters) == len(HANGMAN_PICS) - 1:
        display_board(missed_letters, correct_letters, secret_word)
        print('You have run out of the guesses! \nAfter ' + str(len(missed_letters)) + 'missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "'+ secret_word + '"')

        game_is_done = True

