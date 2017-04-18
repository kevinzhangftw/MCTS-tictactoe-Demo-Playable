from gameStatus import GameStatus
# import networkx as nx


def coordinate(players):
	game = GameStatus()

	# G = initGraph(game)
	round = 0
	while game.winner() is None:
		for player in players:
			round +=1
			print("\n=========(Round #{}. It is {}'s move.)========".format(round, game.turn()))

			game.move(*player.move(game))

			# graph updates
			if game.winner() is not None:
				break
	print('Game over. Winner is {}.'.format(game.winner()))

def initGraph(game):
	graph = nx.DiGraph()
	graph.add_node(str(game))
	root = str(game)
	current = root
	return graph