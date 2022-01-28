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

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        team = team_repository.select(row['team_id'])
        player = Player(team, row['name'], row['position'], row['id'])
        players.append(player)
    return players
