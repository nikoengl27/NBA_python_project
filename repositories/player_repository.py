from unittest import result
from db.run_sql import run_sql
from models.player import Player
from models.team import Team
import repositories.team_repository as team_repository


def save(player):
    sql = "INSERT INTO players (team_id, name, position) VALUES (%s, %s, %s) RETURNING *"
    values = [player.team.id, player.name, player.position]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players ORDER by name ASC"
    results = run_sql(sql)

    for row in results:
        team = team_repository.select(row['team_id'])
        player = Player(team, row['name'], row['position'], row['id'])
        players.append(player)
    return players

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result =run_sql(sql, values)[0]

    if result is not None:
        team = team_repository.select(result['team_id'])
        player = Player(team, result['name'], result['position'], result['id'])
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(player):
    sql = "UPDATE players SET (team_id, name, position) = (%s, %s, %s) WHERE id = %s"
    values = [player.team.id, player.name, player.position, player.id]
    run_sql(sql, values)
