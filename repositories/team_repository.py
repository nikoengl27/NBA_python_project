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

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['stadium'], result['wins'], result['losses'], result['id'] )
    return team

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET (name, stadium, wins, losses) = (%s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.stadium, team. wins, team.losses, team.id]
    run_sql(sql, values)

def players(team):
    players = []

    sql = "SELECT * FROM players WHERE team_id = %s"
    values = [team]
    results = run_sql(sql, values)

    for row in results:
        player = Player(row['team_id'], row['name'], row['position'], row['id'] )
        players.append(player)
    return players