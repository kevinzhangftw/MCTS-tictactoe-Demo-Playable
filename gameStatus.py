import copy

class GameStatus(object):
	def __init__(self):
		self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

	def move(self, row, col):
		print('Move: {} moves to ({}, {})'.format(self.turn(), row, col))
		self.board[row][col] = self.turn()
		print('{}'.format(self))


	def winner(self):
		for player in ['X','O']:
			for row in range(3):
				accum = 0
				for col in range(3):
					if self.board[row][col] == player:
						accum +=1
				if accum == 3:
						return player		
			for col in range(3):
				accum =0
				for row in range(3):
					if self.board[row][col]==player:
						accum +=1
				if accum == 3:
					return player
			#diagonal check
			leftDiagonal = [self.board[0][0],self.board[1][1],self.board[2][2]]
			rightDiagonal = [self.board[2][0],self.board[1][1],self.board[0][2]]
			if all(marker == player for marker in leftDiagonal) \
                    or all(marker == player for marker in rightDiagonal):
				return player
		# tie check
		accum = 0
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == ' ':		
					accum +=1
		if accum == 0:
			return 'Tie'

		return None

	def turn(self):
		numX = 0
		numO = 0
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == 'X':
					numX += 1
				elif self.board[row][col] == 'O':
					numO += 1
			
		if numX == numO:
			return 'X'
		else:
			return 'O'