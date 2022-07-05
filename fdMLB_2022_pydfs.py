from operator import imod
from pydfs_lineup_optimizer import get_optimizer, Site, Sport
from pydfs_lineup_optimizer import stacks, TeamStack, PlayersGroup
optimizer = get_optimizer(Site.FANDUEL, Sport.BASEBALL)

optimizer.load_players_from_csv("D:\Downloads\FanDuel-MLB-2022 ET-07 ET-02 ET-77852-players-list.csv")
for lineup in optimizer.optimize(n=10):
    print(lineup)
    print(lineup.players)  # list of players
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
optimizer.export('DKresult.csv')
