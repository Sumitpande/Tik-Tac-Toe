


board = [" " for i in range(9)]


def display_board():
	row1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
	row2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
	row3 = "| {} | {} | {} |".format(board[6],board[7],board[8])

	print()
	print(row1)
	print(row2)
	print(row3)
	print()


def player_move(c):
	if c == 'X':
		num = 1
	elif c == 'O':
		num = 2

	print("Your turn Player {}".format(num))
	choice = int(input("Enter Your Move (1-9) : ").strip())
	
	if board[choice-1] == " ":
		board[choice-1] = c
	else:
		print()
		print("That Place is taken...")



def is_victory(c):
	if board[0] == c and board[1] == c and board[2] == c or \
	   board[3] == c and board[4] == c and board[5] == c or \
	   board[6] == c and board[7] == c and board[8] == c or \
	   board[0] == c and board[3] == c and board[6] == c or \
	   board[1] == c and board[4] == c and board[7] == c or \
	   board[2] == c and board[5] == c and board[8] == c or \
	   board[0] == c and board[4] == c and board[8] == c or \
	   board[2] == c and board[4] == c and board[6] == c :
	   return True 

	else:
		return False


def is_draw(c):
	if " " not in board :
		return True
	else:
		return False

while True:
	player_move('X')
	display_board()
	if is_victory('X') :
		display_board()
		print("Player X WINS Congrats !!")
		break
	elif is_draw('X'):
		print()
		print("Its draw. Play again..")
		break

	player_move('O')
	display_board()
	if is_victory('O') :
		display_board()
		print("Player O WINS Congrats !!")
		break
	elif is_draw('O'):
		print()
		print("Its draw. Play again..")
		break




