import copy

class GameStatus(object):
	def __init__(self):
		self.board = [[' ', ' ', ' '],
					  [' ', ' ', ' '],
					  [' ', ' ', ' ']]

	def legal_moves(self):
		if self.winner() is not None:
			return []

		possible_moves = []
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == ' ':
					possible_moves.append((row, col))
		return possible_moves

	def transition_function(self, row, col):
		"""
		Applies the specified action to the current state and returns the new
		state that would result. Can be used to simulate the effect of
		different actions. The action is applied to the player whose turn
		it currently is.

		:param state: The starting state before applying the action
		:param row: The row in which to place a marker
		:param col: The column in which to place a marker
		:return: The resulting new state that would occur
		"""
		# Verify that the specified action is legal
		assert (row, col) in self.legal_moves()

		# First, make a copy of the current state
		new_state = copy.deepcopy(self)

		# Then, apply the action to produce the new state
		new_state.move(row, col)

		return new_state

	def __str__(self):	
		output = ''
		for row in range(3):
			for col in range(3):
				contents = self.board[row][col]
				if col < 2:
					output += '{}'.format(contents)
				else:
					output += '{}\n'.format(contents)
		output = output.replace(' ', '~')
		return output


	def move(self, row, col):
		print ('Move: {} moves to ({}, {})'.format(self.turn(), row, col))
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