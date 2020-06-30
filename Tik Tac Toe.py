boad = ["  " in range(9)]


def display_board():
	row1 = "{} | {} | {} ".format(board[0],board[1],board[2])
	row2 = "{} | {} | {} ".format(board[3],board[4],board[5])
	row3 = "{} | {} | {} ".format(board[6],board[7],board[8])

	print()
	print(row1)
	print(row2)
	print(row3)
	print()
