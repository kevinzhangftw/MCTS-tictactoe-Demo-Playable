from humanPlayer import HumanPolicy
from aiPlayer import MCTSPolicy
import coordinator

humanPlayer = HumanPolicy()
aiPlayer = MCTSPolicy(player='X')

players = [aiPlayer, humanPlayer]
coordinator.coordinate(players)


