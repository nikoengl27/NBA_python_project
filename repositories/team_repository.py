from db.run_sql import run_sql
from models.team import Team
from models.player import Player



def save(team):
    sql = "INSERT INTO teams (name, stadium, wins, losses) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [team.name, team.stadium, team.wins, team.losses]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['stadium'], row['wins'], row['losses'], row['id'] )
        teams.append(team)
    return teams