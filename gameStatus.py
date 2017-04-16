import copy

class GameStatus(object):
	def __init__(self):
		self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

	def winner(self):
		#TODO

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