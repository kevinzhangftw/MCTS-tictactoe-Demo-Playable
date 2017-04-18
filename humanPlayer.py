from policy import Policy 

class HumanPolicy(Policy):
    def move(self, state):
        """Chooses moves randomly from the legal moves in a given state"""
        legal_moves = state.legal_moves()
        policyInput = raw_input('Human, enter your next move: ')
        return legal_moves[policyInput]


