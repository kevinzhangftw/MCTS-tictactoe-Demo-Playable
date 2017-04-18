from humanPlayer import HumanPolicy
from aiPlayer import MCTSPolicy
import coordinator

humanPlayer = HumanPolicy()
aiPlayer = MCTSPolicy(player='O')

players = [humanPlayer, aiPlayer]
coordinator.coordinate(players)


