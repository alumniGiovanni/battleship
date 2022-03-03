from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)



for turn in range(4):
  print "Rodada", turn + 1
  guess_row = int(raw_input("Linha: "))
  guess_col = int(raw_input("Coluna: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "No alvo, mandamos os malditos para os tubaroes!"
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Erramos por muito capitao, realinhe os canhoes"
    elif board[guess_row][guess_col] == "X":
      print( "Esse alvo ja foi atingido." )
    else:
      print "Errou!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)