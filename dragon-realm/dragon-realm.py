import random
import time

def displayIntro():
  print()
  print()

def chooseCave():
  cave = ''
  while cave != '1' and cave != '2':
    print('Which cave will you go into? 1 or 2?')
    cave = input()

  return cave

def checkCave(choosenCave):
  print('You approach the cave..')
  time.sleep(2)
  print('It is dark and spooky..')
  time.sleep(2)
  print('A large dragon jumps out in front of you! He opens his jaws and..')
  print()
  time.sleep(2)
