from policy import Policy 
import random
import numpy as np


class HumanPolicy(Policy):
    def move(self, state):
    	print ('human moves here')

    	idx = np.random.randint(len(legal_moves))
    	print ('idx is: {}'.format(idx))

        legal_moves = state.legal_moves()
        
        print ('legal_moves[idx] is: {}'.format(legal_moves[idx])) 

        policyInput = raw_input('Human, enter your next move: ')
        
        return legal_moves[idx]


