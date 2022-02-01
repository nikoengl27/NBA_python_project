from models.player import Player
from models.team import Team
from flask import Flask, redirect, render_template, request
from flask import Blueprint
from repositories import player_repository
from repositories import team_repository
from repositories import standings_repository
import pdb

standings_blueprint = Blueprint("standings", __name__)

@standings_blueprint.route("/standings")
def standings():
    teams = standings_repository.order_teams()
    return render_template("standings/index.html", all_teams = teams, title = "Standings")



