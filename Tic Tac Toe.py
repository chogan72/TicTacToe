#Chris Hogan

import random
player_x = input('Who is player x?')
player_o = 'Computer' #CPU
#player_o = input('Who is player o?') #2Player

board = [['_','_','_'],['_','_','_'],[' ',' ',' ']]

print(board[0][0] + '|' + board[0][1] + '|' + board[0][2] + 
  '\n' + board[1][0] + '|' + board[1][1] + '|' + board[1][2] + 
  '\n' + board[2][0] + '|' + board[2][1] + '|' + board[2][2])

turn = 1
while turn < 10:
  if turn % 2 == 0:
    CPU = 'on'
    while CPU == 'on':
      o_row = random.randint(0, 2) #CPU
      o_column = random.randint(0, 2) #CPU
      #o_row = int(input(player_o + ":Choose a row 1-3")) - 1 #2Player
      #o_column = int(input(player_o + ":Choose a column 1-3")) - 1 #2Player
      if o_row > 2 or o_row < 0 or o_column > 2 or o_column < 0:
        turn = turn - 1
        print ("You can't do that")
      elif board[o_row][o_column] == 'x' or  board[o_row][o_column] == 'o':
        turn = turn - 1
        #print ('Someone is already there') #2Player
      else:
          board[o_row][o_column] = 'o'
          print ("Computer:") #CPU
          CPU = 'off'
        
  else:
    x_row = int(input(player_x + ":Choose a row 1-3")) - 1
    x_column = int(input(player_x + ":Choose a column 1-3")) - 1
    if x_row > 2 or x_row < 0 or x_column > 2 or x_column < 0:
      turn = turn - 1
      print ("You can't do that")
    elif board[x_row][x_column] == 'o' or  board[x_row][x_column] == 'x':
      turn = turn - 1
      print ('Someone is already there')
    else:
        board[x_row][x_column] = 'x'
        
  print(board[0][0] + '|' + board[0][1] + '|' + board[0][2] + 
    '\n' + board[1][0] + '|' + board[1][1] + '|' + board[1][2] + 
    '\n' + board[2][0] + '|' + board[2][1] + '|' + board[2][2])
  turn = turn + 1
  
  if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x' or board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x' or board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x' or board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x' or board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x' or board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x'or board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x' or board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x'or board[0][0] == 'y' and board[0][1] == 'y' and board[0][2] == 'y' or board[1][0] == 'y' and board[1][1] == 'y' and board[1][2] == 'y' or board[2][0] == 'y' and board[2][1] == 'y' and board[2][2] == 'y' or board[0][0] == 'y' and board[1][0] == 'y' and board[2][0] == 'y' or board[0][1] == 'y' and board[1][1] == 'y' and board[2][1] == 'y' or board[0][2] == 'y' and board[1][2] == 'y' and board[2][2] == 'y'or board[0][0] == 'y' and board[1][1] == 'y' and board[2][2] == 'y' or board[2][0] == 'y' and board[1][1] == 'y' and board[0][2] == 'y':
    if turn % 2 == 0:
      print (player_x +' wins')
    else:
      print (player_o + ' wins')
    turn = 11
if turn == 10:
  print('Tie')