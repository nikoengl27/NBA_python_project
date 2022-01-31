from models.player import Player
from flask import Flask, redirect, render_template, request
from flask import Blueprint
from repositories import player_repository
from repositories import team_repository
import pdb

players_blueprint = Blueprint("players", __name__)

#show players
@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", all_players = players)

#show player
@players_blueprint.route("/players/<id>", methods = ['GET'])
def show_player(id):
    player = player_repository.select(id)
    return render_template('players/show.html', player = player)

#new 
@players_blueprint.route("/players/new", methods=['GET'])
def new_player():
    teams = team_repository.select_all()
    return render_template("players/new.html", all_teams = teams)

#create
@players_blueprint.route("/players", methods=['POST'])
def create_player():
    team = team_repository.select(request.form['team_id'])
    name = request.form['name']
    position = request.form['position']
    player = Player(team, name, position)
    player_repository.save(player)
    return redirect('/players')

#edit
@players_blueprint.route("/players/<id>/edit", methods = ['GET'])
def edit_player(id):
    player = player_repository.select(id)
    teams = team_repository.select_all()
    return render_template('players/edit.html', player = player, all_teams = teams)

#update
@players_blueprint.route("/players/<id>", methods = ['POST'])
def update_player(id):
    # pdb.set_trace()
    team = team_repository.select(request.form['team_id'])
    name = request.form['name']
    position = request.form['position']
    player = Player(team, name, position, id)
    player_repository.update(player)
    return redirect('/players')

#delete
@players_blueprint.route("/players/<id>/delete", methods = ['GET'])
def delete_player(id):
    player_repository.delete(id)
    return redirect('/players')

#show players of a team
@players_blueprint.route("/players/team/<id>", methods = ['GET'])
def show_player_of_team(id):
    players = team_repository.players(id)
    return render_template('/players/team_players.html', players = players)

