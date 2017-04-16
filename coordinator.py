from gameStatus import GameStatus

def coordinate(players):
	game = GameStatus() 
	
	round = 0
	while game.winner() is None:
		for player in players:
			round +=1
			print("\n=========(Round #{}. It is {}'s move.)========".format(round, game.turn()))

			pass
		pass