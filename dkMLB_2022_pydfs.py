from operator import imod
from pydfs_lineup_optimizer import get_optimizer, Site, Sport
from pydfs_lineup_optimizer import stacks, TeamStack, PlayersGroup
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASEBALL)

optimizer.load_players_from_csv("D:\Downloads\DKSalaries.csv")
group = PlayersGroup(optimizer.player_pool.get_players(''))
optimizer.add_players_group(group)
for lineup in optimizer.optimize(n=10):
    print(lineup)
    print(lineup.players)  # list of players
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
optimizer.export('DKresult.csv')
