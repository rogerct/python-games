import random
import sys
import math


def get_new_board():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board


def draw_board(board):
  tens_digits_line = '    '

  for i in range(1, 6):
      tens_digits_line += (' ' * 9) + str(i)

  print(tens_digits_line)
  print('  ' + ('0123456789' * 6))
  print()

  for row in range(15):
      if row < 10:
          extra_space = ' '
      else:
          extra_space = ''

      board_row = ''
      for column in range (60):
          board_row += board[column][row]

      print('%s%s %s %s' % (extra_space, row, board_row, row))

  print()
  print('  ' + ('0123456789' * 6))
  print(tens_digits_line)



def get_random_chests(num_chests):
    chests = []
    while len(chests) < num_chests:
      new_chest = [random.randint(0, 59), random.randint(0, 14)]
      if new_chest not in  chests:
          chests.append(new_chest)

    return chests




def get_random_chests(num_chests):
    chests = []
    while len(chests) < num_chests:
      new_chest = [random.randint(0, 59), random.randint(0, 14)]
      if new_chest not in  chests:
          chests.append(new_chest)

    return chests
