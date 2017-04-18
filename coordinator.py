from gameStatus import GameStatus
import networkx as nx


def coordinate(players):
	game = GameStatus()
	
	# Keep track of the game tree
	G = nx.DiGraph()
	# Todo: use the newly implemented hashing method
	G.add_node(str(game))
	root = str(game)
	current = root

	round = 0
	while game.winner() is None:
		for player in players:
			round +=1
			print("\n=========(Round #{}. It is {}'s move.)========".format(round, game.turn()))

			game.move(*player.move(game))

			# wanted to refactor this out but oh well
			previous = current
			G.add_node(str(game))
			current = str(game)
			G.add_edge(previous, current)

			if game.winner() is not None:
				break
	print('Game over. Winner is {}.'.format(game.winner()))

def initGraph(game):
	graph = nx.DiGraph()
	graph.add_node(str(game))
	root = str(game)
	current = root
	return graph

