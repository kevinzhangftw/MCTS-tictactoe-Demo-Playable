from policy import Policy
from gameStatus import GameStatus
import copy
import numpy as np
import operator
import networkx as nx

class MCTSPolicy(Policy):
	def __init__(self, player):
		"""
		Implementation of Monte Carlo Tree Search

		Creates a root of an MCTS tree to keep track of the information
		obtained throughout the course of the game in the form of a tree
		of MCTS nodes

		The data structure of a node consists of:
		  - the game state which it corresponds to
		  - w, the number of wins that have occurred at or below it in the tree
		  - n, the number of plays that have occurred at or below it in the tree
		  - expanded, whether all the children (legal moves) of the node have
			been added to the tree

		To access the node attributes, use the following format. For example,
		to access the attribute 'n' of the root node:
		  policy = MCTSPolicy()
		  current_node = policy.root
		  policy.tree.node[current_node]['n']
		"""
		self.digraph = nx.DiGraph()
		self.player = player
		self.num_simulations = 0
		# Constant parameter to weight exploration vs. exploitation for UCT
		self.uct_c = np.sqrt(2)
		self.uct_c1 = 1
		self.uct_c2 = 2
		self.uct_c3 = 3
		self.uct_c10= 10

		self.node_counter = 0

		empty_board = GameStatus()
		self.digraph.add_node(self.node_counter, attr_dict={'w': 0,
															'n': 0,
															'uct': 0,
															'expanded': False,
															'state': empty_board})
		empty_board_node_id = self.node_counter
		self.node_counter += 1

		self.last_move = None

		if player is 'O':
			for successor in [empty_board.transition_function(*move) for move in empty_board.legal_moves()]:
				self.digraph.add_node(self.node_counter, attr_dict={'w': 0,
																	'n': 0,
																	'uct': 0,
																	'expanded': False,
																	'state': successor})
				self.digraph.add_edge(empty_board_node_id, self.node_counter)
				self.node_counter += 1

	def move(self, starting_state):
		print ('ai goes here')
		starting_state = copy.deepcopy(starting_state)
		# todo: is that copy needed?

		starting_node = None

		if self.last_move is not None:
			# Check if the starting state is already in the graph as a child of the last move that we made
			exists = False
			for child in self.digraph.successors(self.last_move):
				# Check if the child has the same state attribute as the starting state
				if self.digraph.node[child]['state'] == starting_state:
					# If it does, then check if there is a link between the last move and this child state
					if self.digraph.has_edge(self.last_move, child):
						exists = True
						starting_node = child
			if not exists:
				# If it wasn't found, then add the starting state and an edge to it from the last move
				self.digraph.add_node(self.node_counter,
									  attr_dict={'w': 0,
												 'n': 0,
												 'uct': 0,
												 'expanded': False,
												 'state': starting_state})
				self.digraph.add_edge(self.last_move,
									  self.node_counter)
				starting_node = self.node_counter
				self.node_counter += 1
		else:
			for node in self.digraph.nodes():
				if self.digraph.node[node]['state'] == starting_state:
					starting_node = node

		computational_budget = 25

		for i in range(computational_budget):
			self.num_simulations += 1

			print("Running MCTS from this starting state with node id {}:\n{}".format(starting_node,
																					  starting_state))

			# Until computational budget runs out, run simulated trials
			# through the tree:

			# Selection: Recursively pick the best node that maximizes UCT
			# until reaching an unvisited node
			print('================ ( selection ) ================')
			selected_node = self.selection(starting_node)
			print('selected:\n{}'.format(self.digraph.node[selected_node]['state']))

			# Check if the selected node is a terminal state, and if so, this
			# iteration is finished
			if self.digraph.node[selected_node]['state'].winner():
				break

			# Expansion: Add a child node where simulation will start
			print('================ ( expansion ) ================')
			new_child_node = self.expansion(selected_node)
			print('Node chosen for expansion:\n{}'.format(new_child_node))

			# Simulation: Conduct a light playout
			print('================ ( simulation ) ================')
			reward = self.simulation(new_child_node)
			print('Reward obtained: {}\n'.format(reward))

			# Backpropagation: Update the nodes on the path with the simulation results
			print('================ ( backpropagation ) ================')
			self.backpropagation(new_child_node, reward)

		move, resulting_node = self.best(starting_node)
		print('MCTS complete. Suggesting move: {}\n'.format(move))

		self.last_move = resulting_node

		# If we won, reset the last move to None for future games
		if self.digraph.node[resulting_node]['state'].winner():
			self.last_move = None

		return move


