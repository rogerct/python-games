import random

def draw_board(board):

  print(board[7] + '|' + board[8] + '|' + board[9])
  print('-+-+-')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-+-+-')
  print(board[1] + '|' + board[2] + '|' + board[3])

def input_player_letter():

  letter = ''
  while not (letter == 'X' or letter == 'O'):
    print('Do you want to be X or O?')
    letter = input().upper()

  if letter == 'X':
    return ['X', 'O']
  else:
    return ['O', 'X']

def who_goes_first():
  if random.randint(0,1) == 0:
    return 'computer'
  else:
    return 'player'

def make_move(board, letter, move):
  board[move] = letter

def is_winner(bo, le):
  return ((bo[7] == le and bo[8] == le and bo[9] == le) or

  (bo[4] == le and bo[5] == le and bo[6] == le)
  (bo[1] == le and bo[2] == le and bo[3] == le)
  (bo[7] == le and bo[4] == le and bo[1] == le)
  (bo[8] == le and bo[5] == le and bo[2] == le)
  (bo[9] == le and bo[6] == le and bo[3] == le)
  (bo[7] == le and bo[5] == le and bo[3] == le)
  (bo[9] == le and bo[5] == le and bo[1] == le))

def get_board_copy(board):
  board_copy = []
  for i in board:
      board_copy.append(i)
  return board_copy

def is_space_free(board, move):
  return board[move] == ' '

def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not
      is_space_free(board, int(move)):
        print('What is your next move? 1-9')
        move = input()
    return int(move)

def choose_random_move_from_list(board, moves_list):
  possible_moves = []
  for i in moves_list:
    if is_space_free(board, i):
      possible_moves.append(i)

  if len(possible_moves) != 0:
      return random.choice(possible_moves)
  else:
    return None

def get_computer_move(board, computer_letter):

  if computer_letter == 'X':
    player_letter = 'O'
  else:
    player_letter = 'X'

  for i in range(1,10):
     board_copy = get_board_copy(board)
     if is_space_free(board_copy, i):
        make_move(board_copy, player_letter, i)
        if is_winner(board_copy, player_letter):
            return i
  move = choose_random_move_from_list(board, [1, 3, 7, 9])
  if move != None:
    return move

  if is_space_free(board, 5):
      return 5

  return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
  for i in range(1, 10):
      if is_space_free(board, i):
          return False
  return True

print('Welcome to Tic-Tac-Toe!')








