from pydfs_lineup_optimizer import get_optimizer, Site, Sport
from pydfs_lineup_optimizer.stacks import GameStack
from pydfs_lineup_optimizer.stacks import TeamStack
optimizer = get_optimizer(Site.YAHOO, Sport.BASEBALL)
optimizer.load_players_from_csv("D:\Downloads\Yahoo_DF_contest_lineups_insert_template.csv")

optimizer.add_stack(TeamStack(3, for_teams=['LAD'], max_exposure=.1))

lineups = optimizer.optimize(n=3)
for lineup in lineups:
    print(lineup)
optimizer.export('YahooResult.csv')
