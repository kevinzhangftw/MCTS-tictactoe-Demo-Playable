from policy import Policy 
from gameStatus import GameStatus
import random
import numpy as np


class HumanPolicy(Policy):
	def move(self, gameStatus):
		legal_moves = gameStatus.legal_moves()
		print ('Available legal moves are:')
		for i in legal_moves:
		 	print i 
		gameStatus.printBoard()

		policyInput = input('Human, enter your next move: ')
		
		if policyInput < len(legal_moves):
			print ('move legal! please continue')
		else:
			print ('move not allowed! undefined state here')
		
		return legal_moves[policyInput]


