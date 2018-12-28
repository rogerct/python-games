import random
import time

def display_intro():
  print('Hello')
  print()

def choose_cave():
  cave = ''
  while cave != '1' and cave != '2':
    print('Which cave will you go into? 1 or 2?')
    cave = input()

  return cave
def check_cave(choosen_cave):
  print('You approach the cave..')
  time.sleep(2)
  print('It is dark and spooky..')
  time.sleep(2)
  print('A large dragon jumps out in front of you! He opens his jaws and..')
  print()
  time.sleep(2)

  friendly_cave = random.randint(1,2)

  if choosen_cave == str(friendly_cave):
    print('Gives you his treasure!')
  else:
    print('Gobbles you down in one bite!')

play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)
    print('Do you want to play again? yes or no?')
    play_again = input()


