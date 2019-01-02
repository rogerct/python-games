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
  tensDigitsLine = '    '

  for i in range(1, 6):
      tens_
