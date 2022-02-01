from models.player import Player
from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.team import Team
from repositories import player_repository
from repositories import team_repository
import pdb

teams_blueprint = Blueprint("teams", __name__)

#show teams
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", all_teams = teams)

#show team
@teams_blueprint.route("/teams/<id>", methods = ['GET'])
def show_team(id):
    team = team_repository.select(id)
    players = team_repository.players(id)
    return render_template('teams/show.html', team = team, players = players)

#new team
@teams_blueprint.route("/teams/new", methods = ['GET'])
def new_team():
    teams = team_repository.select_all()
    return render_template("teams/new.html", all_teams = teams)

#create team
@teams_blueprint.route("/teams", methods = ['POST'])
def create_team():
    name = request.form['name']
    stadium = request.form['stadium']
    wins = request.form['wins']
    losses = request.form ['losses']
    team = Team(name, stadium, wins, losses)
    team_repository.save(team)
    return redirect('/teams')

#edit team
@teams_blueprint.route("/teams/<id>/edit", methods = ['GET'])
def edit_team(id):
    team = team_repository.select(id)
    return render_template('teams/edit.html', team = team)

#update team
@teams_blueprint.route("/teams/<id>/update", methods = ['POST'])
def update_team(id):
    name = request.form['name']
    stadium = request.form['stadium']
    wins = request.form['wins']
    losses = request.form['losses']
    team = Team(name, stadium, wins, losses, id)
    team_repository.update(team)
    return redirect('/teams')

#delete team
@teams_blueprint.route("/teams/<id>/delete", methods = ['GET'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')


