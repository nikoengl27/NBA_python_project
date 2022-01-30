from db.run_sql import run_sql
from models.team import Team
from models.player import Player


def order_teams():
    teams = []

    sql = "SELECT * FROM teams ORDER by wins DESC"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['stadium'], row['wins'], row['losses'], row['id'] )
        teams.append(team)
    return teams