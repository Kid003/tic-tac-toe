# Auxillary checking method
def check(board):
	for row in board:
		item = row[0]
		if item:
			if row.count(item) == len(row):
				return item

	return False

class Board:
	def __str__(self):
		head = '   a  b  c'
		result = '\n'.join([str(idx) + ' ' +  str(row) for idx, row in enumerate(self.board)])
		return head + '\n' + result

	def __init__(self, board):
		self.board = board

	def move(self, player, row, col, show = True):
		self.board[row][col] = player
		if show:
			print(self)

	def check_winners(self):
		return self.check_rows() or self.check_cols() or self.check_diags()

	def check_rows(self):
		return check(self.board)

	def check_cols(self):
		column_board = []

		for i in range(len(self.board)):
			column_board.append([row[i] for row in self.board])
			
		return check(column_board)

	def check_diags(self):

		d1 = [row[index] for index, row in enumerate(self.board)]
		d2 = [row[2-index] for index, row in enumerate(self.board)]
		diag_board = [d1,d2]
		return check(diag_board)