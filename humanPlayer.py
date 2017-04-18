from policy import Policy 
from gameStatus import GameStatus
import random
import numpy as np


class HumanPolicy(Policy):
	def move(self, state):
		print ('human moves here')

		legal_moves = state.legal_moves()
		idx = np.random.randint(len(legal_moves))
		print ('idx is: {}'.format(idx))
		print ('legal_moves[idx] is: {}'.format(legal_moves[idx])) 

		policyInput = raw_input('Human, enter your next move: ')
		# convert the string to a move
		# Verify that the specified action is legal
		# assert (row, col) in self.legal_moves()
		# return the index of that move
		
		return legal_moves[idx]


